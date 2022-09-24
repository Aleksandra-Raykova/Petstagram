from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from petstagram.accounts.models import Profile
from petstagram.common.forms import CommentForm
from petstagram.common.views import get_photos_likes_info
from petstagram.photos.forms import CreatePhotoForm, EditPhotoForm
from petstagram.photos.models import Photo


@login_required
def add_photo(request):
    form = CreatePhotoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        photo = form.save(commit=False)
        photo.created_by_user = request.user.profile
        photo.save()
        form.save_m2m()

        return redirect('home')

    context = {"form": form}

    return render(request=request, template_name='photos/photo-add-page.html', context=context)


def show_photo_details(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    profile = Profile.objects.get(user_id=photo.created_by_user)
    total_likes_count = photo.like_set.count()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        "profile": profile,
        "photo": photo,
        "total_likes_count": total_likes_count,
        "comments": comments,
        "comment_form": comment_form,
        "photos_likes_info": get_photos_likes_info(request, [photo]),
    }

    return render(request=request, template_name='photos/photo-details-page.html', context=context)


@login_required
def edit_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == "GET":
        form = EditPhotoForm(initial=photo.__dict__)
    else:
        form = EditPhotoForm(request.POST, instance=photo)

        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {'form': form}

    return render(request=request, template_name='photos/photo-edit-page.html', context=context)


@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()

    return redirect('home')

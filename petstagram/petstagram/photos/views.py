from django.shortcuts import render, redirect, get_object_or_404

from petstagram.accounts.models import Profile
from petstagram.common.forms import CommentForm
from petstagram.photos.forms import CreatePhotoForm, EditPhotoForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = CreatePhotoForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user_profile = request.user
        pet.save()
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
        "comment_form": comment_form
    }

    return render(request=request, template_name='photos/photo-details-page.html', context=context)


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


def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('home')

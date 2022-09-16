from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo

from pyperclip import copy


def show_home_page(request):
    photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            photos = photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        "all_photos": list(photos)[::-1],
        "comment_form": comment_form,
        "search_form": search_form,
    }

    return render(request=request, template_name='common/home-page.html', context=context)


@login_required
def add_comment_view(request, photo_pk):
    if request.method == 'POST':
        photo_object = Photo.objects.get(pk=photo_pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo_object
            comment.user = request.user.profile
            comment.save()

        return redirect(request.META['HTTP_REFERER'])


@login_required
def like_functionality(request, photo_pk):
    photo = Photo.objects.get(pk=photo_pk)
    like_object_by_user = photo.like_set.filter(user_id=request.user.id).first()

    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')


def copy_link_to_clipboard(request, photo_pk):
    if "#" in str(request.META['HTTP_REFERER']):
        copy(request.META['HTTP_REFERER'])
    else:
        copy(request.META['HTTP_REFERER'] + f'#{photo_pk}')

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')

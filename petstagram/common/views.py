from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo

from clipboard import copy


def get_photos_likes_info(request, photos):
    photos_likes_info = []

    for photo in photos:
        if photo.like_set.filter(user_id=request.user.id).first():
            photos_likes_info.append(photo.id)

    return photos_likes_info


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
        "photos_likes_info": get_photos_likes_info(request, photos),
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
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_pk))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')

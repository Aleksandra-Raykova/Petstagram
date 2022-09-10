from django.shortcuts import render, redirect, get_object_or_404

from petstagram.common.forms import CommentForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def show_home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    context = {"all_photos": all_photos, "comment_form": comment_form}
    return render(request=request, template_name='common/home-page.html', context=context)


def add_comment_view(request, photo_pk):
    if request.method == 'POST':
        photo_object = Photo.objects.get(pk=photo_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo_object
            comment.user = request.user
            comment.save()
        return redirect('home')  # TODO check is can redirect to the same page no matter which one it is


def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    like_object_by_user = photo.like_set.filter(user_id=request.user.id).first()
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(photo=photo, user=request.user)
        like.save()
    return redirect('pet-details', photo_id)

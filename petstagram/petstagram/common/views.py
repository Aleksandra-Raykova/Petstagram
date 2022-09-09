from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
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
        return redirect('home')

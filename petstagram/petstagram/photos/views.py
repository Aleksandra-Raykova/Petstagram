from django.shortcuts import render, redirect, get_object_or_404

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
    # TODO add likes and comments for this photo
    photo = get_object_or_404(Photo, pk=pk)
    context = {"photo": photo}
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

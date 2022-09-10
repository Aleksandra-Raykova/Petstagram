from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user_profile = request.user
        pet.save()
        return redirect('home')
    context = {"form": form}
    return render(request=request, template_name='pets/pet-add-page.html', context=context)


def show_pet_details(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug, user_profile__username=username)
    photos = get_list_or_404(Photo, tagged_pets__name=pet.name)
    context = {"pet": pet, "photos": photos}
    return render(request=request, template_name='pets/pet-details-page.html', context=context)


def edit_pet(request, username, pet_slug):
    return render(request=request, template_name='pets/pet-edit-page.html')


def delete_pet(request, username, pet_slug):
    return render(request=request, template_name='pets/pet-delete-page.html')

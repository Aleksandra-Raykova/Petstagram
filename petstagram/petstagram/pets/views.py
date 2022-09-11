from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from petstagram.pets.forms import PetForm, DeletePetForm
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def get_pet_object(user, pet):
    return get_object_or_404(Pet, slug=pet, user_profile__slug=user)


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user_profile = request.user
        pet.save()
        return redirect('home')
    context = {"form": form}
    return render(request=request, template_name='pets/pet-add-page.html', context=context)


def show_pet_details(request, user_slug, pet_slug):
    pet = get_pet_object(user_slug, pet_slug)
    photos = get_list_or_404(Photo, tagged_pets__name=pet.name)
    context = {"pet": pet, "photos": photos}
    return render(request=request, template_name='pets/pet-details-page.html', context=context)


def edit_pet(request, user_slug, pet_slug):
    pet = get_pet_object(user_slug, pet_slug)
    if request.method == "GET":
        form = PetForm(initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', user_slug, pet_slug)
    context = {'form': form}
    return render(request=request, template_name='pets/pet-edit-page.html', context=context)


def delete_pet(request, user_slug, pet_slug):
    pet = get_pet_object(user_slug, pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('home')

    form = DeletePetForm(instance=pet)
    context = {'form': form}
    return render(request=request, template_name='pets/pet-delete-page.html', context=context)

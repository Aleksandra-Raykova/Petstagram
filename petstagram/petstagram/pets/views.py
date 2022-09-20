from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from petstagram.accounts.models import Profile
from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetForm, DeletePetForm
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


UserModel = get_user_model()


def get_pet_object(user, pet):
    return get_object_or_404(Pet, slug=pet, user_profile__user__username=user)


@login_required
def add_pet(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        pet = form.save(commit=False)
        user = request.user.profile
        pet.user_profile = user
        pet.save()

        return redirect('profile-details', pk=request.user.pk)

    context = {"form": form}

    return render(request=request, template_name='pets/pet-add-page.html', context=context)


def show_pet_details(request, username, pet_slug):
    user = UserModel.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    pet = get_pet_object(username, pet_slug)
    photos = list(Photo.objects.filter(tagged_pets__slug=pet.slug))[::-1]
    comment_form = CommentForm()

    context = {
        "profile": profile,
        "pet": pet,
        "all_photos": photos,
        "comment_form": comment_form,
    }

    return render(request=request, template_name='pets/pet-details-page.html', context=context)


@login_required
def edit_pet(request, username, pet_slug):
    pet = get_pet_object(username, pet_slug)

    if request.method == "GET":
        form = PetForm(initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {'form': form}

    return render(request=request, template_name='pets/pet-edit-page.html', context=context)


@login_required
def delete_pet(request, username, pet_slug):
    pet = get_pet_object(username, pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=request.user.pk)

    form = DeletePetForm(instance=pet)
    context = {'form': form}

    return render(request=request, template_name='pets/pet-delete-page.html', context=context)

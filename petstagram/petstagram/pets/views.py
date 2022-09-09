from django.shortcuts import render, redirect

from petstagram.pets.forms import PetForm


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request=request, template_name='pets/pet-add-page.html', context=context)


def show_pet_details(request):
    return render(request=request, template_name='pets/pet-details-page.html')


def edit_pet(request):
    return render(request=request, template_name='pets/pet-edit-page.html')


def delete_pet(request):
    return render(request=request, template_name='pets/pet-delete-page.html')

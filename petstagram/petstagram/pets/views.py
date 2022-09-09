from django.shortcuts import render


def add_pet(request):
    return render(request=request, template_name='pets/pet-add-page.html')


def show_pet_details(request):
    return render(request=request, template_name='pets/pet-details-page.html')


def edit_pet(request):
    return render(request=request, template_name='pets/pet-edit-page.html')


def delete_pet(request):
    return render(request=request, template_name='pets/pet-delete-page.html')

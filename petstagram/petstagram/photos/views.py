from django.shortcuts import render


def add_photo(request):
    return render(request=request, template_name='photos/photo-add-page.html')


def show_photo_details(request):
    return render(request=request, template_name='photos/photo-details-page.html')


def edit_photo(request):
    return render(request=request, template_name='photos/photo-edit-page.html')

from django.contrib.auth import urls
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from petstagram.main_app.forms import *
from petstagram.main_app.models import Profile, PetPhoto, Pet


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login-page.html'
    next_page = 'dashboard'


def check_profile(function):
    def wrapper(request, *args, **kwargs):
        if not Profile.objects.first():
            return render(request=request, template_name='401_error.html', status=401, )
        return function(request, *args, **kwargs)

    return wrapper


def index(request):
    my_user = User.objects.get(username='some_user')
    print(my_user.has_perm('main_app.add_pet'))
    try:
        profile = Profile.objects.first()
    except IndexError:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, 'home_page.html', context)


def create_profile(request):
    print(request.user.__class__.__name__)
    logout(request)
    print(request.user.__class__.__name__)
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        user_form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-page')
        else:
            context = {'form': form, 'user_form': user_form}
            return render(request, 'profile_create.html', context)

    form = CreateProfileForm()
    user_form = UserForm(request.POST)
    context = {'form': form, 'user_form': user_form}
    return render(request, 'profile_create.html', context)


@check_profile
def dashboard(request):
    pets_photos = PetPhoto.objects.all()
    context = {
        'pets_photos': pets_photos,
    }
    return render(request, 'dashboard.html', context)


@check_profile
def add_photo(request):
    if request.method == 'POST':
        form = CreateImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = CreateImageForm()
    context = {'form': form}
    return render(request, 'image_create.html', context)


@check_profile
def add_pet(request):
    if request.method == 'POST':
        form = CreatePetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.profile = Profile.objects.first()
            pet.save()
            return redirect('profile-page')

    form = CreatePetForm()
    context = {'form': form}
    return render(request, 'pet_create.html', context)


@check_profile
def photo_details(request, photo_id):
    pet_photo = PetPhoto.objects.get(id=photo_id)
    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'image_detail.html', context)


@check_profile
def add_likes(request, photo_id):
    pet_photo = PetPhoto.objects.get(id=photo_id)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo-details-page', photo_id=photo_id)


@check_profile
def profile_page(request):
    profile = Profile.objects.first()
    pets = Pet.objects.filter(profile=profile.id)
    images = PetPhoto.objects.all()
    total_images_number = len(images)
    total_likes_number = sum(map(lambda i: i.likes, images))
    context = {
        'profile': profile,
        'pets': pets,
        'total_images_number': total_images_number,
        'total_likes_number': total_likes_number,
    }
    return render(request, 'profile_details.html', context)


@check_profile
def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == "GET":
        context = {'form': ChangeProfileForm(initial=profile.__dict__)}
        return render(request, 'profile_edit.html', context)
    else:
        form = ChangeProfileForm(request.POST, instance=profile)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('profile-page')
        else:
            context = {'form': form}
            return render(request, 'profile_edit.html', context)


@check_profile
def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.all()[0]
        profile.delete()
        PetPhoto.objects.all().delete()
        return redirect('index-page')
    return render(request, 'profile_delete.html')


@check_profile
def edit_photo(request, photo_id):
    photo = PetPhoto.objects.get(id=photo_id)
    if request.method == "GET":
        context = {'form': ChangeImageForm(
            initial={
                'description': photo.description,
                'pet': [p for p in photo.pet.all()]}),
            'photo': photo}
        return render(request, 'image_edit.html', context)
    else:
        form = ChangeImageForm(request.POST, instance=photo)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            context = {'form': form, 'photo': photo}
            return render(request, 'image_edit.html', context)


@check_profile
def delete_photo(request, photo_id):
    photo = PetPhoto.objects.get(id=photo_id)
    photo.delete()
    return redirect(dashboard)


@check_profile
def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == "GET":
        context = {'form': CreatePetForm(initial=pet.__dict__)}
        return render(request, 'pet_edit.html', context)
    else:
        form = CreatePetForm(request.POST, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile-page')
        else:
            context = {'form': form}
            return render(request, 'pet_edit.html', context)


@check_profile
def delete_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-page')

    form = DeletePetForm(instance=pet)
    context = {
        'form': form
    }
    return render(request, 'pet_delete.html', context)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path, include

from petstagram.main_app.views import *

urlpatterns = [
                  path('', index, name='index-page'),
                  path('create-profile/', create_profile, name='profile-create'),
                  path('profile/', profile_page, name='profile-page'),
                  path('dashboard', dashboard, name='dashboard'),
                  path('add-pet/', add_pet, name='pet-create'),
                  path('add-photo/', add_photo, name='photo-create'),
                  path('photo/<int:photo_id>/', photo_details, name='photo-details-page'),
                  path('edit-photo/<int:photo_id>/', edit_photo, name='photo-edit'),
                  path('edit-pet/<int:pet_id>/', edit_pet, name='pet-edit'),
                  path('add-one-like/<int:photo_id>/', add_likes, name='add-one-like'),
                  path('delete-photo/<int:photo_id>/', delete_photo, name='photo-delete'),
                  path('delete-profile/', delete_profile, name='profile-delete'),
                  path('delete-pet/<int:pet_id>/', delete_pet, name='pet-delete'),
                  path('create-profile/', create_profile, name='profile-create'),
                  path('edit-profile/', edit_profile, name='profile-edit'),
                  path('profile/', profile_page, name='profile-page'),
                  path('login/', CustomLoginView.as_view(), name='login-page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

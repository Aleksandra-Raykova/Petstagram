from django.urls import path
from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='add-pet'),
    path('<slug:user_slug>/pet/<slug:pet_slug>/', views.show_pet_details, name='pet-details'),
    path('<slug:user_slug>/pet/<slug:pet_slug>/edit/', views.edit_pet, name='edit-pet'),
    path('<slug:user_slug>/pet/<slug:pet_slug>/delete/', views.delete_pet, name='delete-pet'),
]

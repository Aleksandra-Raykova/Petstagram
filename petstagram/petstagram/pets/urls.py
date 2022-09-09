from django.urls import path
from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='add-pet'),
    path('owner<str:username>/pet/<slug:pet_name>/', views.show_pet_details, name='pet-details'),
    path('owner<str:username>/pet/<slug:pet_name>/edit', views.edit_pet, name='edit-pet'),
    path('owner<str:username>/pet/<slug:pet_name>/delete', views.delete_pet, name='delete-pet'),
]

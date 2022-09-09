from django.urls import path
from petstagram.pets import views

urlpatterns = [
    path('owner<str:username>/pet/add/', views.add_pet, name='add-pet'),
    path('owner<str:username>/pet/<slug:pet_name>/', views.show_pet_details, name='create-pet'),
    path('owner<str:username>/pet/<slug:pet_name>/edit', views.edit_pet, name='edit-pet'),
    path('owner<str:username>/pet/<slug:pet_name>/delete', views.delete_pet, name='delete-pet'),
]

from django.urls import path
from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='photo-add-page'),
    path('<int:pk>/', views.show_photo_details, name='photo-details-page'),
    path('edit/<int:pk>/', views.edit_photo, name='photo-edit-page'),
]

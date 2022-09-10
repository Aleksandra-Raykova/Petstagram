from django.urls import path

from petstagram.accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.show_profile_details, name='change password'),
    path('profile/<str:username>/edit/', views.edit_profile, name='profile'),
    path('profile/<str:username>/delete/', views.delete_profile, name='edit view'),
]

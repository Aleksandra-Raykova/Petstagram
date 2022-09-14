from django.urls import path
from petstagram.accounts import views
from .signals import *


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/<slug:slug>/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('profile/<slug:slug>/edit/', views.edit_profile_view, name='edit-profile'),
    path('profile/<slug:slug>/delete/', views.DeleteProfileView.as_view(), name='delete-profile'),
]

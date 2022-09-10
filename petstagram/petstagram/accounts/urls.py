from django.urls import path

from petstagram.accounts import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/<str:username>/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('profile/<slug:slug>/edit/', views.EditProfileView.as_view(), name='edit-profile'),
    path('profile/<slug:slug>/delete/', views.DeleteProfileView.as_view(), name='delete-profile'),
]

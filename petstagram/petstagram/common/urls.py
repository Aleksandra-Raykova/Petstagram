from django.urls import path
from petstagram.common import views


urlpatterns = [
    path('', views.show_home_page, name='home'),
]

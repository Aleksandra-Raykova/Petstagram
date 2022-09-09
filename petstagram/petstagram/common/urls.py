from django.urls import path
from petstagram.common import views


urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('<int:photo_pk>/', views.add_comment_view, name='add-comment')
]

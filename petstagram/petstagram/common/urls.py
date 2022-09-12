from django.urls import path
from petstagram.common import views
from django.conf.urls.static import static
from petstagram import settings

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('comment/<int:photo_pk>/', views.add_comment_view, name='add-comment'),
    path('like/<int:photo_pk>/', views.like_functionality, name='like'),
    path('share/<int:photo_pk>/', views.copy_link_to_clipboard, name='share'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

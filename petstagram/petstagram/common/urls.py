from django.urls import path
from petstagram.common import views
from django.conf.urls.static import static
from petstagram import settings

urlpatterns = [
                  path('', views.show_home_page, name='home'),
                  path('<int:photo_pk>/', views.add_comment_view, name='add-comment'),
                  path('<int:photo_pk>/', views.like_functionality, name='like'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from petstagram.restapp.views import *

urlpatterns = [

    path('pets/', PetListCreate.as_view(), ),
    path('pets/<int:pet_id>/', PetGetUpdateDelete.as_view(), ),
    path('pets-photos/', PetPhotoListCreate.as_view(), ),
    path('pets-photos/<int:pet_photo_id>/', PetPhotoGetUpdateDelete.as_view(), ),

]

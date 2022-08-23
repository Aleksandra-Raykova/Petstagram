from django.contrib import admin

from petstagram.restapp.models import Profile, Pet, PetPhoto

admin.site.register(Pet)
admin.site.register(PetPhoto)
admin.site.register(Profile)

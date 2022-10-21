from django.contrib import admin
from petstagram.photos import models


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "created_by_user", "get_tagged_pets", "date_of_publication")

    @staticmethod
    def get_tagged_pets(obj):
        return [pet for pet in obj.tagged_pets.all()]


admin.site.register(models.Photo, PhotoAdmin)

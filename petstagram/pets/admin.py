from django.contrib import admin
from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth", "user_profile", "pet_photos_count", "slug")

    @staticmethod
    def pet_photos_count(obj):
        return obj.photo_set.count()


admin.site.register(Pet, PetAdmin)

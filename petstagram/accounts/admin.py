from django.contrib import admin
from petstagram.accounts import models


class PetstagramUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "date_joined")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "user")


admin.site.register(models.PetstagramUser, PetstagramUserAdmin)
admin.site.register(models.Profile, ProfileAdmin)

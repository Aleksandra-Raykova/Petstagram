from django.contrib import admin
from petstagram.accounts import models
# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.PetstagramUser)

from django.contrib import admin
from petstagram.photos import models


admin.site.register(models.Comment)
admin.site.register(models.Photo)

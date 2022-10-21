from django.contrib import admin

from petstagram.common import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "user", "created_on")


class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "photo", "created_by_user")

    @staticmethod
    def created_by_user(obj):
        return obj.photo.created_by_user


admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Like, LikeAdmin)

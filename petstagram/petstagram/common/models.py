from django.db import models

from petstagram.accounts.models import Profile, PetstagramUser
from petstagram.photos.models import Photo


class Comment(models.Model):
    body = models.TextField(max_length=300)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE)
    created_or_edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_or_edited_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body[:10], self.user.username)


class Like(models.Model):
    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)

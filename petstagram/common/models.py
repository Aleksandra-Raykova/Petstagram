from django.db import models

from petstagram.accounts.models import Profile, PetstagramUser
from petstagram.photos.models import Photo


class Comment(models.Model):
    body = models.TextField(max_length=300)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'by {}'.format(self.user.get_user_name())


class Like(models.Model):
    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)

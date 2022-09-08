from django.db import models

from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet


class Photo(models.Model):
    photo_file = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=300)
    likes = models.IntegerField(default=0, editable=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True, editable=False)
    tagged_pets = models.ManyToManyField(to=Pet)


class Comment(models.Model):
    body = models.TextField(max_length=300)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    created_or_edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_or_edited_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body[:10], self.user.first_name)

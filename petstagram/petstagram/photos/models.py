from django.db import models
from petstagram.pets.models import Pet


class Photo(models.Model):
    photo_file = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=300)
    likes = models.IntegerField(default=0, editable=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True, editable=False)
    tagged_pets = models.ManyToManyField(to=Pet)


class Comment(models.Model):
    comment = models.TextField(max_length=300)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)

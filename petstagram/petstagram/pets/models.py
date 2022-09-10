from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from petstagram.accounts.models import PetstagramUser


class Pet(models.Model):
    name = models.CharField(max_length=20)  # TODO pet names should be unique per user
    date_of_birth = models.DateField()  # TODO to be calendar to choose dates from
    pet_photo = models.URLField()
    slug = models.SlugField()
    user_profile = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

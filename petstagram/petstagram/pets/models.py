from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Pet(models.Model):
    name = models.CharField(
        max_length=6
    )
    date_of_birth = models.DateField()
    slug = models.SlugField()
    user_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

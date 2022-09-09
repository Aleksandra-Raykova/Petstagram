from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from petstagram.accounts.models import PetstagramUser


class Pet(models.Model):
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    slug = models.SlugField(blank=True)
    user_profile = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
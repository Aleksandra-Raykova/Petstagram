from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify

from petstagram.accounts.models import PetstagramUser, Profile


class Pet(models.Model):
    name = models.CharField(
        max_length=20,
    )

    date_of_birth = models.DateField()

    pet_photo = models.URLField()

    slug = models.SlugField()

    user_profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )

    def clean(self):
        name = self.name

        if name in [pet.name for pet in Pet.objects.filter(name=name).exclude(pk=self.pk)]:
            raise ValidationError('You already have a pet with this name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

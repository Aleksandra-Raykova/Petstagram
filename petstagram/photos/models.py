from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


class Photo(models.Model):
    photo_file = models.ImageField(
        verbose_name="Pet Photo",
        upload_to='images',
        validators=[
            validate_file_size,
        ]
    )

    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(10),
        )
    )

    date_of_publication = models.DateField(
        auto_now=True,
        editable=False,
        null=True
    )

    tagged_pets = models.ManyToManyField(
        verbose_name="Tag Pets",
        to=Pet,
        blank=True,
    )

    created_by_user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )

    photo_shooting_location = models.CharField(
        verbose_name="Location",
        max_length=50,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['date_of_publication']

    def __str__(self):
        return '{} by {}'.format(self.id, self.created_by_user.get_user_name() or self.created_by_user.user)

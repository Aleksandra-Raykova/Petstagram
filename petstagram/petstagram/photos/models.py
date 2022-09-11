from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet


class Photo(models.Model):
    photo_file = models.ImageField(verbose_name="Pet Photo", upload_to='images/')  # TODO max size 5MB
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),))
    date_of_publication = models.DateField(auto_now_add=True, editable=False, null=True)
    tagged_pets = models.ManyToManyField(verbose_name="Tag Pets", to=Pet)
    created_by_user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    photo_shooting_location = models.CharField(max_length=50, null=True,
                                               blank=True)  # TODO check how can be added google map locations

    class Meta:
        ordering = ['date_of_publication']

    def __str__(self):
        return '{} by {}'.format(self.description[:10], self.created_by_user.get_user_name())

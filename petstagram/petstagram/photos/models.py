from django.db import models

from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet


class Photo(models.Model):
    photo_file = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=300)
    likes = models.IntegerField(default=0, editable=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True, editable=False)
    tagged_pets = models.ManyToManyField(to=Pet)
    created_by_user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    photo_shooting_location = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['date_time_of_publication']

    def __str__(self):
        return 'Photo {} by {}'.format(self.description[:10], self.created_by_user.get_full_name())

from datetime import date

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.main_app.custom_validators import only_letters_validator, validate_image

animal_types = [
    ('cat', 'Cat'),
    ('dog', 'Dog'),
    ('bunny', "Bunny"),
    ('parrot', 'Parrot'),
    ('fish', 'Fish'),
    ('other', 'Other')
]

genders = [
    ('male', 'Male'),
    ('female', 'Female'),
    (None, 'Do not show'),
]


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator,
        ],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator,
        ]
    )
    profile_picture = models.URLField()
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=30, choices=genders, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Pet(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=animal_types)
    birthday = models.DateField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['profile', 'name'],
                name='unique name'
            )
        ]

    @property
    def age(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
            return str(age)

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    photo = models.ImageField(upload_to='images/', validators=[validate_image])
    description = models.TextField(null=True, blank=True)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, editable=False)
    pet = models.ManyToManyField(Pet)

    def __str__(self):
        return self.description

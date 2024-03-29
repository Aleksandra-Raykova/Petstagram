from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models
from petstagram.accounts.managers import PetstagramUserManager
from petstagram.accounts.validators import validate_isalpha


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_USERNAME_LEN = 25

    username = models.CharField(max_length=25, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    MAX_NAME_LEN = 25
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    email = models.EmailField(
        unique=True,
    )

    user = models.OneToOneField(
        to=PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=(
            MinLengthValidator(2),
            validate_isalpha
        ),
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=(
            MinLengthValidator(2),
            validate_isalpha
        ),
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=11,
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW
    )

    def get_user_name(self):
        name = None
        if self.first_name and self.last_name:
            name = '%s %s' % (self.first_name, self.last_name)
        elif self.first_name:
            name = '%s' % self.first_name
        elif self.last_name:
            name = '%s' % self.last_name
        return name

    def email_user(self, subject, message, from_email=None, **kwargs):
        ...

    def __str__(self):
        user_info = '%s %s' % (self.user.username, self.get_user_name())
        return user_info

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models
from petstagram.accounts.managers import PetstagramUserManager


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    email = models.EmailField(unique=True)
    user = models.OneToOneField(to=PetstagramUser, on_delete=models.CASCADE, primary_key=True)

    first_name = models.CharField(max_length=30, validators=(MinLengthValidator(2),), null=True, blank=True)
    last_name = models.CharField(max_length=30, validators=(MinLengthValidator(2),), null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    gender = models.CharField(max_length=11, choices=GENDERS, null=True, blank=True, default=DO_NOT_SHOW)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        ...

    def __str__(self):
        user_info = '%s %s' % (self.user.username, self.get_full_name())
        return user_info

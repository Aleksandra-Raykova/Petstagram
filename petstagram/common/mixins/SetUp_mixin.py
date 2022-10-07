from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo

UserModel = get_user_model()


class SetUpMixin(TestCase):
    def setUp(self):
        self.user = UserModel(
            username='softuni-pets',
            password='softuni-python-web',
        )

        self.user.full_clean()
        self.user.save()

        self.profile = Profile(
            user=self.user,
            email="softuni-petstagram@softuni.com",
        )

        self.profile.full_clean()
        self.profile.save()

        self.pet = Pet(
            name="Axolotl",
            pet_photo="https://i.natgeofe.com/n/de94c416-6d23-45f5-9708-e8d56289268e/naturepl_01132178.jpg?w=636&h=631",
            user_profile=self.profile,
            slug="Axolotl"
        )

        self.pet.full_clean()
        self.pet.save()

        self.photo = Photo(
            photo_file=SimpleUploadedFile(
                name='test_image.jpg',
                content=open('./petstagram/photos/tests/models/images/dambo.jpg', 'rb').read(),
                content_type='image/jpeg'
            ),
            created_by_user=self.profile
        )

        self.photo.full_clean()
        self.photo.save()

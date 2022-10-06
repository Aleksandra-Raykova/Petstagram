from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


UserModel = get_user_model()


class PhotoModelTests(TestCase):
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

    def test_photo_model_create__with_valid_data__expect_success(self):
        photo = Photo()
        photo.created_by_user = self.profile
        photo.photo_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./petstagram/photos/tests/models/images/dambo.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        photo.full_clean()
        photo.save()

        photo.tagged_pets.set([self.pet])
        photo.save()

        self.assertIsNotNone(photo.pk)
        self.assertEqual(photo.tagged_pets.count(), 1)

    def test_photo_with_bigger_photo_file_than_5MB__except_fail(self):
        photo = Photo()
        photo.created_by_user = self.profile
        photo.photo_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./petstagram/photos/tests/models/images/6MB.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        with self.assertRaises(ValidationError) as context:
            photo.full_clean()
            photo.save()

        self.assertIsNotNone(context.exception)

    def test_description_less_than10_but_more_than_0_symbols__expect_fail(self):
        photo = Photo()
        photo.created_by_user = self.profile
        photo.description = 'd' * 9
        photo.photo_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./petstagram/photos/tests/models/images/dambo.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        with self.assertRaises(ValidationError) as context:
            photo.full_clean()
            photo.save()

        self.assertIsNotNone(context.exception)

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from petstagram.common.mixins.SetUp_mixin import SetUpMixin
from petstagram.photos.models import Photo


class PhotoModelTests(SetUpMixin):
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

    def test_description_less_than_10_but_more_than_0_symbols__expect_fail(self):
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

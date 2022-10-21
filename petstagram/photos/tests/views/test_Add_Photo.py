from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from petstagram.common.mixins.SetUp_mixin import SetUpMixin
from petstagram.photos.models import Photo


class AddPhotoViewTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("photo-add-page"))
        self.assertTemplateUsed(response, 'photos/photo-add-page.html')

    def test_get__expect_form_in_context(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("photo-add-page"))
        self.assertIn('form', response.context)

    def test_post__except_redirect_to_home(self):
        self.client.force_login(self.user)

        photo_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./petstagram/photos/tests/images/dambo.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        response = self.client.post(reverse("photo-add-page"), {'photo_file': photo_file})
        self.assertRedirects(response, reverse("home"))

    def test_post__expect_photo_model_save(self):
        self.client.force_login(self.user)

        photos_len = len(Photo.objects.all())

        photo_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./petstagram/photos/tests/images/dambo.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        self.client.post(reverse("photo-add-page"), {'photo_file': photo_file})
        self.assertEqual(photos_len + 1, len(Photo.objects.all()))

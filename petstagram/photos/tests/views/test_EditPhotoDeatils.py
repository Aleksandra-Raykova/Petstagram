from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from petstagram.common.mixins.SetUp_mixin import SetUpMixin
from petstagram.photos.models import Photo


class EditPhotoViewTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("edit-photo", kwargs={"pk": self.photo.pk}))
        self.assertTemplateUsed(response, "photos/photo-edit-page.html")

    def test_get__expect_form_in_context(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("edit-photo", kwargs={"pk": self.photo.pk}))
        self.assertIn('form', response.context)

    def test_post__except_redirect_to_photo_details(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse("edit-photo", kwargs={"pk": self.photo.pk}))
        self.assertRedirects(response, reverse("photo-details", kwargs={"pk": self.photo.pk}))

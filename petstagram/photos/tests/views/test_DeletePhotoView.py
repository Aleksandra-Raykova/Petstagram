from django.urls import reverse
from petstagram.common.mixins.SetUp_mixin import SetUpMixin
from petstagram.photos.models import Photo


class DeletePhotoViewTests(SetUpMixin):
    def test_post__expect_delete_photo(self):
        self.client.force_login(self.user)
        self.client.post(reverse("delete-photo", kwargs={"pk": self.photo.pk}))

        with self.assertRaises(Photo.DoesNotExist) as dne:
            Photo.objects.get(id=self.photo.id)

        self.assertIsNotNone(dne.exception)

    def test_post__except_redirect_to_home(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse("delete-photo", kwargs={"pk": self.photo.pk}))
        self.assertRedirects(response, reverse("home"))

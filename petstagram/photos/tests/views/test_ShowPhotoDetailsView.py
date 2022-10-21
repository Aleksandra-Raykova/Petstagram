from django.urls import reverse
from petstagram.common.mixins.SetUp_mixin import SetUpMixin


class ShowPhotoDetailsViewTests(SetUpMixin):
    def test_get__expect_correct_template(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("photo-details", kwargs={'pk': self.photo.pk}))
        self.assertTemplateUsed(response, "photos/photo-details-page.html")

    def test_get__expect_correct_context(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("photo-details", kwargs={'pk': self.photo.pk}))

        self.assertIn("profile", response.context)
        self.assertIn("photo", response.context)
        self.assertIn("total_likes_count", response.context)
        self.assertIn("comments", response.context)
        self.assertIn("comment_form", response.context)
        self.assertIn("photos_likes_info", response.context)

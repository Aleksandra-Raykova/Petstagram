from petstagram.common.mixins.SetUp_mixin import SetUpMixin
from petstagram.photos.forms import EditPhotoForm


class EditPhotoFormTests(SetUpMixin):
    def test_photo_field_disabled__expect_true(self):
        form = EditPhotoForm(instance=self.photo, initial=self.photo.__dict__)

        with self.assertRaises(KeyError) as ke:
            photo_field = form.fields["photo_file"]

        self.assertIsNotNone(ke.exception)

    def test_edit_description__expect_success(self):

        form = EditPhotoForm(
            instance=self.photo,
            initial=self.photo.__dict__,
            data={
                "description": "What a nice creature is that dumbo octopus."
            }
        )

        form.is_valid()
        form.save()

        self.assertEqual(self.photo.description, "What a nice creature is that dumbo octopus.")

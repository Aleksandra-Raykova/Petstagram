from django.core.files.uploadedfile import SimpleUploadedFile
from petstagram.common.mixins.SetUp_mixin import SetUpMixin
from petstagram.photos.forms import CreatePhotoForm


class CreatePhotoFormTests(SetUpMixin):
    def test_valid_form(self):
        photo_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=open('./petstagram/photos/tests/images/dambo.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        form_data = {
            "description": "That's a cool dumbo octopus",
            "photo_shooting_location": "Deep Sea",
            "tagged_pets": [self.pet]
        }

        form = CreatePhotoForm(form_data, {"photo_file": photo_file})

        self.assertTrue(form.is_valid())

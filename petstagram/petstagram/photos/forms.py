from django import forms

from petstagram.photos.models import Photo


class CreatePhotoForm(forms.ModelForm):
    photo_file = forms.FileField()

    class Meta:
        model = Photo
        fields = ['photo_file', 'description', 'photo_shooting_location', 'tagged_pets']
        labels = {
            "photo_shooting_location": "Location"
        }


class EditPhotoForm(CreatePhotoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            if field == 'photo':
                field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'

    class Meta(CreatePhotoForm.Meta):
        fields = ['photo_file', 'description', 'photo_shooting_location', 'tagged_pets']
        labels = {
            "photo_shooting_location": "Location"
        }


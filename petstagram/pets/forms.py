from django import forms
from django.utils.text import slugify

from petstagram.pets.models import Pet


class DateInput(forms.DateInput):
    input_type = 'date'


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'pet_photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': DateInput(),
            'pet_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }

class DeletePetForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

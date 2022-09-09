from django import forms
from django.utils.text import slugify

from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user_profile = self.user
        pet.slug = slugify(pet.name)
        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        fields = '__all__'

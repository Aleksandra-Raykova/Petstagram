from django import forms
from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user_profile = self.user

        if commit:
            pet.save()

        return pet

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    image = forms.FileField(required=True, widget=forms.FileInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-2'
    }))

    class Meta:
        model = Pet
        fields = ('name', 'description', 'image')

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from petstagram.main_app.models import Profile, PetPhoto, Pet
from datetime import date


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter password again'})
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].required = None
        self.fields['password1'].required = None
        self.fields['password2'].required = None

    class Meta:
        model = User
        fields = ('username',)
        labels = {
            "username": "Username",
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username',
                }),
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()  # running sql in database to store data
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "profile_picture": "Link to Profile Picture",
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }),
            'profile_picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }),
        }


class CreateImageForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'pet')
        labels = {
            "photo": "Pet Image",
            "description": "Description",
            "pet": "Tag Pets",
        }
        widgets = {
            "photo": forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3,
                }),
            'pet': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class CreatePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'birthday')
        labels = {
            "name": "Pet Name",
            "type": "Type",
            "birthday": "Day of Birth",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
            'birthday': forms.SelectDateWidget(
                years=range(1990, date.today().year + 1),
                attrs={
                    'class': 'form-control',
                }),
        }


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture', 'date_of_birth', 'email', 'gender', 'description')
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "profile_picture": "Link to Profile Picture",
            'date_of_birth': "Date of Birth",
            'email': 'Email',
            'gender': 'Gender',
            'description': 'Description',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }),
            'profile_picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }),
            'date_of_birth': forms.SelectDateWidget(
                years=range(1920, date.today().year + 1),
                attrs={
                    'class': 'form-control',
                }),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                }),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3,
                }),
        }


class DeletePetForm(CreatePetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class ChangeImageForm(CreateImageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            if field == 'photo':
                field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'

    class Meta(CreateImageForm.Meta):
        exclude = ('photo',)

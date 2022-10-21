from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet
from django.contrib.auth.forms import AuthenticationForm


UserModel = get_user_model()


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password'}
        )


class CreateProfileForm(auth_forms.UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Username'}
        )
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email'}
        )
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Repeat password'}
        )

    def clean_email(self):
        email = self.cleaned_data['email']

        if email in [p.email for p in Profile.objects.all()]:
            raise forms.ValidationError('User with that email already exists')

        return email

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(email=self.cleaned_data['email'], user=user)

        if commit:
            profile.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class EditUserForm(forms.ModelForm):
    username = forms.CharField(max_length=UserModel.MAX_USERNAME_LEN)

    class Meta:
        model = UserModel
        fields = ['username']
        labels = {"first_name": "First Name", "last_name": "Last Name"}


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'gender']
        labels = {"first_name": "First Name", 'last_name': "Last Name", "profile_picture": "Image"}


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        # Not good
        # should be done with signals
        # because this breaks the abstraction of the auth app
        user = UserModel.objects.get(id=self.instance.id)
        pets = list(self.instance.pet_set.all())
        Pet.objects.filter(tagged_pets__in=pets).delete()

        user.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()

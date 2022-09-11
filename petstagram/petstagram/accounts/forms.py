from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet
from django.contrib.auth.forms import AuthenticationForm


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

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(email=self.cleaned_data['email'], user=user)
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=Profile.MAX_NAME_LEN)
    first_name = forms.CharField(max_length=Profile.MAX_NAME_LEN)
    last_name = forms.CharField(max_length=25)
    picture = forms.URLField()
    date_of_birth = forms.DateField()
    gender = forms.ChoiceField(choices=Profile.GENDERS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = Profile
        exclude = ('slug',)


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        # Not good
        # should be done with signals
        # because this breaks the abstraction of the auth app
        pets = list(self.instance.pet_set.all())
        Pet.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()

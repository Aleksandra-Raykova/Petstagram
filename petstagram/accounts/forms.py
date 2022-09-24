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
    first_name = forms.CharField(max_length=Profile.MAX_NAME_LEN)
    last_name = forms.CharField(max_length=Profile.MAX_NAME_LEN)
    profile_picture = forms.URLField()
    gender = forms.ChoiceField(choices=Profile.GENDERS, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['profile_picture'].required = False
        self.fields['gender'].required = False

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if not first_name.isalpha():
            raise forms.ValidationError('First name can only contain letters.')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if not last_name.isalpha():
            raise forms.ValidationError('Last name can only contain letters.')

        return last_name

    class Meta:
        model = Profile
        exclude = ('slug', 'user', 'date_of_birth')


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
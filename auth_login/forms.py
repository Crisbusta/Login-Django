from django import forms
from auth_login import views
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='email', required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'           
        ]
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = (self.cleaned_data["first_name"])
        user.last_name = (self.cleaned_data["last_name"])
        user.email = (self.cleaned_data["email"])

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]

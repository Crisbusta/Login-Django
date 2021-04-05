from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.Form):
    username = forms.CharField(label='username')
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    email = forms.EmailField(label='email')
    password =  forms.CharField(label='password', widget=forms.PasswordInput, max_length=100) 
    #address = forms.CharField(label='address')
    #phone = forms.IntegerField(label='phone')
    #city =  forms.CharField(label='city')
    #rut =  forms.CharField(label='Rut')
    #age = forms.IntegerField()
    #birth_date = forms.DateField(label='Birth date', widget=forms.DateInput, help_text="e.g. YYYY-MM-DD")

class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = {
            'email',
            'first_name',
            'last_name',
            'password'
        }

class EditUserProfile(forms.Form):
    username = forms.CharField(label='username')
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    email = forms.EmailField(label='email')
    password =  forms.CharField(label='password', widget=forms.PasswordInput, max_length=100) 
    address = forms.CharField(label='address')
    phone = forms.IntegerField(label='phone')
    city =  forms.CharField(label='city')
    #rut =  forms.CharField(label='Rut')
    #age = forms.IntegerField()
    #birth_date = forms.DateField(label='Birth date', widget=forms.DateInput, help_text="e.g. YYYY-MM-DD")
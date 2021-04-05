from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.Form):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='E-Mail')
    password =  forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100) 
    #rut =  forms.CharField(label='Rut')
    #address = forms.CharField(label='Address')
    #age = forms.IntegerField()
    #birth_date = forms.DateField(label='Birth date', widget=forms.DateInput, help_text="e.g. YYYY-MM-DD")
    #phone = forms.IntegerField(label='Phone')
    #country =  forms.CharField(label='Country')

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

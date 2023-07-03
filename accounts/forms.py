from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', max_length=30, required=False)
    last_name = forms.CharField(label='Last Name', max_length=30, required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "avatar"]
        help_texts = { key: '' for key in fields }


class UserUpdateForm(forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='First Name', max_length=30, required=False)
    last_name = forms.CharField(label='Last Name', max_length=30, required=False)
    avatar = forms.ImageField(required=False)

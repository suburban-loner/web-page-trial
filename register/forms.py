from django import forms
from django.contrib.auth import login, authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=140)

    class Meta:
        model = User
        fields = ['name', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'username', 'password1', 'password2']



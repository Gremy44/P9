from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nom d'utilisateur")
    password = forms.CharField(
        max_length=50, widget=forms.PasswordInput, label="Mot de passe")


class Registration(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ['username']


class FindUser(forms.Form):
    username = forms.CharField(max_length=50, label="Nom d'utilisateur")

    class Meta:
        model = models.User
        fields = ['username']

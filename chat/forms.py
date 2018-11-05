from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from . import models

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
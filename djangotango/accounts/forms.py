from . import models
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class UserFormCreate(UserCreationForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

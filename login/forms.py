from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Profile
from django.forms import ModelForm 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user','username']
class CreateUserform(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username','email','password1','password2']

    

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
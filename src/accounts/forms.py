from django import forms
from django.forms import fields 
from . import models
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class  Meta:
        model=User
        fields=['username','first_name','last_name','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['ProImage','ProCountry','ProAddress']
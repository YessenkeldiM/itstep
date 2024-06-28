from django import forms
from .models import User


class UserForm(forms.Form):
    name = forms.CharField(max_length=200, label = 'Name')
    surname = forms.CharField(max_length=20, label = 'Surname')
    gender = forms.CharField( max_length=20)
    adult = forms.BooleanField()




from django import forms
from .models import User
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    name = forms.CharField(max_length=200, label = 'Name')
    surname = forms.CharField(max_length=20, label = 'Surname')
    gender = forms.CharField( max_length=20)
    adult = forms.BooleanField()

    def cleaned_name(self):
        name = self.cleaned_data['name']
        if name == 'Miras':
            raise ValidationError('Нельзя зарегестрироваться с именем Мирас')
        else:
            return name




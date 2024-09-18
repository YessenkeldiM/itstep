from django.shortcuts import render
from .forms import UserProfileForm
from django.views.generic import CreateView
from .models import UserProfile

# Create your views here.


class CreateProfile(CreateView):
    template_name = 'userprofile/index.html'
    model = UserProfile
    fields = '__all__'
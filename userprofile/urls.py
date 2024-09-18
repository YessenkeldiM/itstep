from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.CreateProfile.as_view(), name="index"),
]
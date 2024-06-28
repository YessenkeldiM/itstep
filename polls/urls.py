from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: polls/all/
    path("all/", views.all, name="all"),
    path("all/hello/", views.all_hello, name="all_hello"),
    # ex: polls/first/2/
    path("first/<int:question_number>/", views.number, name="first-N"),
    # ex: polls/search/hello/
    path("search/<slug:search_text>/", views.search_text, name="search"),
]
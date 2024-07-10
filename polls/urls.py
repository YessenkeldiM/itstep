from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    path('helloworld/', views.HelloWorldView.as_view(), name="hello-world"),
    path('first-detail/', views.QuestionDetailTemplateView.as_view(), name='first-detail'),
    path('redirect/<int:question_id>/', views.QuestionRedirectView.as_view(), name='redirect'),
    path('detail/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('choice-list/<int:votes>/', views.ChoiceList.as_view(), name='choice-list'),
    path('question/create/', views.QuesitonFormView.as_view(), name='create-question'),
    path('question/create2/', views.QuestionCreateView.as_view(), name='create-question2'),
    path('question/update/<int:pk>/', views.QuestionUpdateView.as_view(), name='update-question'),
    path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view(), name='delete-question'),
    path('questions/', views.QuestionListView.as_view(), name='question-list')
    # ex: polls/all/
    # path("all/", views.all, name="all"),
    # path("all/hello/", views.all_hello, name="all_hello"),
    # ex: polls/first/2/
    # path("first/<int:question_number>/", views.number, name="first-N"),
    # ex: polls/search/hello/
    # path("search/<slug:search_text>/", views.search_text, name="search"),
]
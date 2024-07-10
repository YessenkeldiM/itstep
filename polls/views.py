from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from .models import Question, Choice
from .forms import QuestionForm
from django.db.models import Count, Min
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseNotFound, HttpResponseForbidden, Http404
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import FormView, CreateView, UpdateView, DeleteView

def index(request):
    res = ''
    for i in dir(request):
        res = res + str(getattr(request,i)) + ', '
    return HttpResponse(res)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def all_hello(request):
    return HttpResponse('This is all HELLO VIEW!')

def all(request):
    return HttpResponse('This is all VIEW!')
    # questions = Question.objects.all()
    # return render(request, "polls/index.html", {"questions": questions})

def get_number() -> int:
    return 5


def number(request, question_number):
    if request.method == 'POST':
        ...
    elif request.method == 'GET':
        ...
    else:
        ...
    questions = Question.objects.all()[:question_number]
    return render(request, "polls/index.html", {"questions": questions})




def search_text(request, search_text):
    questions = Question.objects.filter(question_text__contains=search_text)
    return render(request, "polls/index.html", {"questions": questions})


def latest(request):
    q = Question.objects.latest()
    return render(request, polls/index.html, {'info': q})

def counter(request):
    q = Question.objects.all().count()
    return render(request, polls/index.html, {'info': q})

def votes_agr(request):
    q = Question.objects.aggregate(Count('votes'))
    return render(request, polls/index.html, {'info': q})

def votes_ann(request):
    q = Question.objects.annotate(min_voting=Min('votes'))
    return render(request, polls/index.html, {'info': q})

def get_avg(request):
    q = Question.objects.aggregate()


class HelloWorldView(View):
    allowed_http_methods = ['get']
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world!')
    

class QuestionDetailTemplateView(TemplateView):
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.first()
        context['message'] = 'Hello world'
        return {'message': '!@#$'}
    
class QuestionRedirectView(RedirectView):
    query_string = False
    pattern_name = 'polls:first-detail'

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        try:
            q = Question.objects.get(pk=kwargs['question_id'])
        except Question.DoesNotExist:
            kwargs.pop('question_id')
            return super().get_redirect_url(*args, **kwargs)
    

class QuestionDetail(DetailView):
    template_name = 'polls/detail.html'
    model = Question

    def get_queryset(self):
        return self.model.objects.filter('pub_date'>2023)
    
    def get_object(self, queryset):
        return self.queryset.filter(question_id=kwargs['question_id'])
    

class ChoiceList(ListView):
    template_name = 'polls/list_detail.html'
    model = Choice
    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs)

    def get_queryset(self):
        q = super().get_queryset().filter(votes__gt=self.kwargs['votes'])
        return q
    

class QuesitonFormView(FormView):
    template_name = 'polls/create.html'
    form_class = QuestionForm
    # model = Question
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self) -> str:
        url = self.object.instance.get_absolute_url()
        return url
    
class QuestionCreateView(CreateView):
    template_name = 'polls/create.html'
    model = Question
    fields = '__all__'


class QuestionUpdateView(UpdateView):
    template_name = 'polls/update.html'
    model = Question
    fields = ['question_text']
    success_url = reverse_lazy('polls:question-list')

class QuestionDeleteView(DeleteView):
    template_name = 'polls/delete.html'
    model = Question
    success_url = reverse_lazy('polls:question-list')

class QuestionListView(ListView):
    template_name = 'polls/question_list.html'
    model = Question


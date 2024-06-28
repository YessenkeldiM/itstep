from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Question
from django.db.models import Count, Min


def index(request):
    # return HttpResponse('Hello world!')
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # context = {"questions": latest_question_list, 'name': 'SANDUGASH'}
    return render(request, "polls/index.html", {})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # questiom 
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
    if request.POST:
        ...
    elif request.GET:
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
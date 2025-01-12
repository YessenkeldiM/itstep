from django.shortcuts import render, HttpResponse
from .forms import UserForm

# Create your views here.


def index(request):
    user_form = UserForm()
    context = {'form': user_form}
    return HttpResponse('Hello world')
    return render(request, 'users/index.html', context)


def add_user(request):
    user_form = UserForm(request.POST)
    if user_form.is_valid():    
        message = 'User is saved'
        context = {'form': user_form, 'message': message}
        return render(request, 'users/index.html', context)
    

def index_and_add_user(request):
    if request.method == 'GET':
        index(request)
    else:
        add_user(request)


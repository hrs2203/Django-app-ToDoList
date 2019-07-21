from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.http import HttpRequest , HttpResponse , Http404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from todo.models import Task , TaskType
from todo.forms import NewTaskForm , NewTaskTypeForm

def homepage(request):
    return render(
        request = request,
        template_name = 'todo/homepage.html',
        context={}
    )

def logout_request(request):
    logout(request)
    messages.success(request , 'logout succesfully')
    return redirect('/')

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request=request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request , 'login succesfully')
                return redirect('/account/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm
    return render(
        request = request,
        template_name = 'todo/login.html',
        context={
            'form' : form,
        }
    )

def register_request(request):

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request , 'user created succesfully')
            username = form.cleaned_data.get("username")
            User.objects.filter(username = username).update(is_superuser=True , is_staff=True)
            login(request , user)
            messages.success(request , 'login succesfully')
            return redirect('/')
        else:
            messages.error(request, "Something went wrong. Invalid username or password.")
            
    form = UserCreationForm
    return render(
        request = request,
        template_name = 'todo/registration.html',
        context={
            'form' : form,
        }
    )

def account_details(request):
    username = None
    tasks = []
    task_title = TaskType.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        tasks =  Task.objects.filter( user_detail_id = User.objects.get(username=username).id )
         
    return render(
        request = request,
        template_name = 'todo/account.html',
        context= { 
            'tasks' : tasks,
            'task_type' : task_title,
        }
    )

def add_new_task(request):
    if request.method=='POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('/account/')
            messages.success(request , 'Task added Succesfully')
        else:
            messages.error(request , "Something went wrong. please try again")

    form = NewTaskForm
    return render(
        request = request,
        template_name = 'todo/edition.html',
        context={
            'form' : form,
        }
    )

def add_new_task_type(request):
    if request.method=='POST':
        form = NewTaskTypeForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('/account/')
            messages.success(request , 'Task Type added Succesfully')
        else:
            messages.error(request , "Something went wrong. please try again")

    form = NewTaskTypeForm
    return render(
        request = request,
        template_name = 'todo/edition.html',
        context={
            'form' : form,
        }
    )
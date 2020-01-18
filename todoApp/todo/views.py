from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from todo.forms import NewTaskForm, NewTaskTypeForm
from todo.models import Task, TaskType


def homepage(request):
    tasks = Task.objects.all()
    tasks = tasks[:12]
    return render(
        request = request,
        template_name = 'todo/homepage.html',
        context={ 'tasks' : tasks }
    )

def logout_request(request):
    logout(request)
    messages.success(request , 'logout succesfully')
    return redirect('/todo/')

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
                return redirect('/todo/account/')
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
            return redirect('/todo/')
        else:
            messages.error(request, "Something went wrong. Invalid username or password.")
            
    form = UserCreationForm()
    return render(
        request = request,
        template_name = 'todo/registration.html',
        context={
            'form' : form,
        }
    )

def account_details(request):
    # username = None
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
    if request.user.is_authenticated:
        if request.method=='POST':
            form = NewTaskForm(request.POST)
            if form.is_valid():
                form.instance.user_detail_id = request.user.id
                form.save()
                return redirect('/todo/account/')
                messages.success(request , 'Task added Succesfully')
            else:
                messages.error(request , "Something went wrong. please try again")

        form = NewTaskForm(initial = {'user_detail': request.user})
        return render(
            request = request,
            template_name = 'todo/edition.html',
            context={
                'form' : form,
            }
        )
    return render (
        request = request,
        template_name= "todo/user_not_found.html",
        context= {}
    )

def add_new_task_type(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = NewTaskTypeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Task Type added Succesfully')
                return redirect('/todo/account/')
            else:
                messages.error(request , "Something went wrong. please try again")

        form = NewTaskTypeForm()
        return render(
            request = request,
            template_name = 'todo/edition.html',
            context={
                'form' : form,
            }
        )
    return render (
        request=request,
        template_name="todo/user_not_found.html",
        context={}
    )


def edit_task(request):
    id = int(request.GET['id'])

    data = Task.objects.filter(id=id)
    if len(data)!=0:
        data = data[0]
        if data.user_detail_id == request.user.id:
            if request.method == 'POST':
                form = NewTaskForm(request.POST)
                if form.is_valid():
                    data.user_detail = request.user
                    data.task_type = form.cleaned_data['task_type']
                    data.task_description = form.cleaned_data['task_description']
                    data.task_status = form.cleaned_data['task_status']
                    data.start_time = form.cleaned_data['start_time']
                    data.end_time = form.cleaned_data['end_time']
                    data.save()
                    messages.success(request, 'Task edited Succesfully')
                    return redirect('/todo/account/')
                else:
                    messages.error(request, "Something went wrong. please try again")

            
            task_data = {
                'user_detail' : data.user_detail,
                'task_type' : data.task_type,
                'task_description': data.task_description,
                'task_status': data.task_status,
                'start_time': data.start_time,
                'end_time': data.end_time
            }
            form = NewTaskForm(initial = task_data)
            return render(
                request=request,
                template_name='todo/edition.html',
                context={
                    'form': form,
                }
            )
    return render (
        request=request,
        template_name="todo/user_not_found.html",
        context={}
    )

def delete_task(request):
    id=int(request.GET['id'])
    data = Task.objects.filter(id=id)
    data.delete()
    messages.success(request, "Deletion successfull")
    return redirect('/todo/account/')

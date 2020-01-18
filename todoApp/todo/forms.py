from todo.models import Task, TaskType
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
# from datetime import datetime , timedelta


class NewTaskTypeForm(ModelForm):
    class Meta:
        model = TaskType
        fields = '__all__'


class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_type','task_description','task_status','start_time','end_time']

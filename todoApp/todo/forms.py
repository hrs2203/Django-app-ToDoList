from todo.models import TaskType , Task
from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
# from datetime import datetime , timedelta

class NewTaskTypeForm(ModelForm):
    class Meta:
        model = TaskType
        fields = '__all__'
        
class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

from todo.models import TaskType , Task
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime , timedelta

class NewTaskTypeForm(ModelForm):
    class Meta:
        model = TaskType
        fields = '__all__'
        
class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

# class NewTaskTypeForm(forms.Form):
#     task_type = forms.CharField()
#     task_type_description = forms.CharField( widget=forms.Textarea() )

# class NewTaskForm(forms.Form):
#     user_detail = forms.ModelChoiceField(queryset=User.objects)
#     task_type = forms.ModelChoiceField(queryset=TaskType.objects)
#     task_description = forms.CharField(widget=forms.Textarea())
#     task_status = forms.BooleanField()
#     start_time = forms.DateTimeField()
#     end_time = forms.DateTimeField()

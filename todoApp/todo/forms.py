from todo.models import TaskType , Task
from django.forms import ModelForm

class NewTaskTypeForm(ModelForm):
    class Meta:
        model = TaskType
        fields = [  'task_type_description' , 'task_type']
        
class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


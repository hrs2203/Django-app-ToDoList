from django.db import models
from django.contrib.auth.models import User
from datetime import datetime , timedelta
from tinymce import HTMLField

class TaskType(models.Model):
    task_type = models.CharField(max_length=50)
    task_type_description = HTMLField("content")

class Task(models.Model):
    user_detail = models.ForeignKey( User , on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType , null=True , blank=True , default=None , on_delete=models.SET_DEFAULT)
    task_description = HTMLField("content")
    task_status = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default = datetime.now() + timedelta(days = 1))
from django.db import models
from django.contrib.auth.models import User


class TaskType(models.Model):
    task_type = models.CharField(max_length=50)
    task_type_description = models.TextField()


class Task(models.Model):
    user_detail = models.ForeignKey( User , on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType , null=True , blank=True , default=None, on_delete=models.SET_DEFAULT)
    task_description = models.TextField()
    task_status = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
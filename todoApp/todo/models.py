from django.db import models
from django.contrib.auth.models import User


class TaskType(models.Model):
    task_type = models.CharField(max_length=50)
    task_type_description = models.TextField()

    def __str__(self):
        return self.task_type
    


class Task(models.Model):
    user_detail = models.ForeignKey( User , on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType , null=True , blank=True , default=None, on_delete=models.SET_DEFAULT)
    task_description = models.TextField(default="working on something")
    task_status = models.BooleanField(default=False)
    start_time = models.DateTimeField(default="2019-08-20 06:55:55")
    end_time = models.DateTimeField(default="2019-08-20 06:55:55")

    def __str__(self):
        return self.task_description[:10] + "..."
    
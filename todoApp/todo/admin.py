from django.contrib import admin
from todo import models

admin.site.register(models.TaskType)
admin.site.register(models.Task)

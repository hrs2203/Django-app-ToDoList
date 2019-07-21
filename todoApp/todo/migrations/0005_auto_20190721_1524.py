# Generated by Django 2.2.3 on 2019-07-21 15:24

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20190721_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 22, 15, 24, 3, 248021)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=tinymce.models.HTMLField(verbose_name='content'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-03 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_tasklist_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 23, 58, 45, 661192)),
        ),
    ]

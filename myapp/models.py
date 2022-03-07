from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class tasklist(models.Model):
    manager= models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    task=models.CharField(max_length=150)
    done=models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now(), blank=True)
    due = models.DateTimeField(default=datetime.now(), blank=True)




    def __str__(self):
        return self.task





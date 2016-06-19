from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.TextField(max_length=120)
    description = models.TextField()
    is_done = models.BooleanField()


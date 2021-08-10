from django.db import models
from django.db.models.fields import BooleanField, DateTimeField, TextField

class Task(models.Model):
    body = models.TextField()
    estimated_finish_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



from django.db import models
from django.db.models.fields import BooleanField, DateTimeField, TextField
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    body = models.TextField()
    estimated_finish_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



from django.db import models
from uuid import uuid4

from accounts.models import Account

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.IntegerField(blank=True)

class UserTodo(Todo):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
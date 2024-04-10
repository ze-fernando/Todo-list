from django.db import models
from user.models import User


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

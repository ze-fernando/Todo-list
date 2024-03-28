from django.db import models
from datetime import datetime
from user.models import User


class Task(models.Model):
    __tablename__ = 'tasks'


    name=models.CharField(max_length=25)
    done=models.BooleanField()
    created_at=models.DateField(default=datetime.now())
    user=models.ForeignKey(User, on_delete=models.CASCADE)

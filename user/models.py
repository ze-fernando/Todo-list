from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager


class User(AbstractBaseUser):

    username = models.TextField(unique=True)
    password = models.TextField()
    age = models.IntegerField()
    tel = models.IntegerField(unique=True, default=0)

    objects = CustomUserManager()

    last_login = None

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"User:{self.username=} {self.age=} {self.tel=}"

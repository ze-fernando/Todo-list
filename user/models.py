from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class User(AbstractBaseUser):

    user_name = models.TextField()
    password = models.TextField()
    age = models.IntegerField()

    objects = UserManager()

    last_login = None


    USERNAME_FIELD = 'id'


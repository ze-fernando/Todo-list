from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):

    user_name = models.TextField()
    password = models.TextField()
    age = models.IntegerField()

    last_login = None


    USERNAME_FIELD = 'id'


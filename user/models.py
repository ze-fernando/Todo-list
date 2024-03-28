from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):

    user_name = models.CharField(max_lenght=25)
    password = models.CharField()
    age = models.IntegerField()

    last_login = None


    USERNAME_FIELD = 'id'


from django.db import models


class User(models.Model):
    user_name=models.CharField(max_lenght=25)
    password=models.CharField()
    age=models.IntegerField()
    

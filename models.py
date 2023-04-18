from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=5)
    age = models.CharField(max_length=13)


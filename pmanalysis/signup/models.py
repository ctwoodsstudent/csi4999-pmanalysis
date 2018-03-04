from django.db import models
from django.contrib.auth.models import User

class UserFiles(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Descr = models.CharField(max_length=150)
    Org = models.CharField(max_length=150)
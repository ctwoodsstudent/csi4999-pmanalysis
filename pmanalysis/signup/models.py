from django.db import models
from django.contrib.auth.models import User

class UserFiles(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=50)
    Descr = models.CharField(max_length=150)
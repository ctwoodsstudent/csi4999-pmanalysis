from django.db import models
from django.contrib.auth.models import User

class UserFiles(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Descr = models.CharField(max_length=150)
    Org = models.CharField(max_length=150)
    def __str__(self):
        return self.Name

class GEOStudy(models.Model):
    Dataset = models.CharField(max_length=100)
    Title = models.CharField(max_length=500)
    Organism = models.CharField(max_length=100)
    Platform = models.CharField(max_length=100)
    Series = models.CharField(max_length=100)
    NumSamples = models.IntegerField()
    Contributors = models.CharField(max_length=100)
    PubDate = models.DateField()
    Link = models.CharField(max_length=500)
    def __str__(self):
        return self.Title

class Report(models.Model):
    Name = models.CharField(max_length=100)
    Pval = models.FloatField()
    Tails = models.IntegerField()
    CInterval = models.FloatField()
    def __str__(self):
        return self.Name


class UserGEO(models.Model):
    Dataset = models.CharField(max_length=100)
    Title = models.CharField(max_length=500)
    Organism = models.CharField(max_length=100)
    Platform = models.CharField(max_length=100)
    Series = models.CharField(max_length=100)
    NumSamples = models.IntegerField()
    Contributors = models.CharField(max_length=100)
    PubDate = models.DateField()
    Link = models.CharField(max_length=500)
    def __str__(self):
        return self.Title

from django.db import models
from django.contrib.auth.models import User

#User uploaded files
class UserFiles(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Descr = models.CharField(max_length=150)
    Org = models.CharField(max_length=150)
    def __str__(self):
        return self.Name

#The contents of our GEO lite database
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

#Reports generated that the user saves
class Report(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Pval = models.FloatField()
    Tails = models.IntegerField()
    CInterval = models.FloatField()
    def __str__(self):
        return self.Name

#Files User selects from GEO Database
class UserGEO(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
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

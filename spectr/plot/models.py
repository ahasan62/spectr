from django.db import models
from django.contrib.postgres.fields import ArrayField

import string 
# Create your models here.
class Normalized(models.Model):
    molecule = models.CharField(max_length=50,default="")
    isocode =  models.CharField(max_length=50,default="")
    velocity =  models.CharField(max_length=50,default="")
    thermal =  models.CharField(max_length=50,default="")
    profile = models.CharField(max_length=50,default="",unique=True)
    temperature =  models.CharField(max_length=8,default="")
    log_columndensity =models.CharField(max_length=50,default="")
    # normalized = md(models.FloatField(),default=list)
    normalized = models.TextField()
    # normalized = models.CharField()
    def __str__(self):
        return self.name

    # normalized = models.FloatField(default=1)

class Emission(models.Model):
    molecule = models.CharField(max_length=50,default="")
    isocode =  models.CharField(max_length=50,default="")
    velocity =  models.CharField(max_length=50,default="")
    thermal =  models.CharField(max_length=50,default="")
    profile =  models.CharField(max_length=50,default="")
    temperature =  models.CharField(max_length=50,default="")
    log_columndensity =  models.CharField(max_length=50,default="")
    emission = models.TextField()
    def __str__(self):
        return self.name
    

class Wavelength(models.Model):
    oversampling = models.CharField(max_length=50,default="")
    resolution = models.CharField(max_length=50,default="")
    wavelength = models.TextField()
    def __str__(self):
        return self.name



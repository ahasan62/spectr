from django.db import models
from django.contrib.postgres.fields import ArrayField

import string 
# Create your models here.
class Normalized(models.Model):
    molecule = models.CharField(max_length=50,default="")
    isocode =  models.IntegerField()
    velocity =  models.FloatField()
    thermal =  models.IntegerField()
    profile = models.CharField(max_length=50,default="",unique=True)
    temperature =  models.FloatField()
    log_columndensity =models.FloatField()
    normalized = ArrayField(models.FloatField(),default=list)
    # normalized = models.JSONField(default=dict)

    # normalized = models.CharField()
    def __str__(self):
        return self.molecule

    # normalized = models.FloatField(default=1)

class Emission(models.Model):
    molecule = models.CharField(max_length=50,default="")
    isocode =  models.IntegerField()
    velocity =  models.FloatField()
    thermal =  models.IntegerField()
    profile =  models.CharField(max_length=50,default="")
    temperature =  models.FloatField()
    log_columndensity =models.FloatField()
    emission = ArrayField(models.FloatField(),default=list)

    def __str__(self):
        return self.molecule
    

class Wavelength(models.Model):
    oversampling = models.IntegerField()
    resolution = models.FloatField()
    wavelength = ArrayField(models.FloatField(),default=list)
    def __str__(self):
        return self.resolution



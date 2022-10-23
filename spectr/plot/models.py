from django.db import models
from django.contrib.postgres.fields import ArrayField

import string 
# Create your models here.
class Normalized(models.Model):
    molecule = models.CharField(max_length=8,default="")
    isocode = models.IntegerField(null=False,default=1221)
    velocity = models.FloatField(null=False)
    thermal = models.FloatField(null=False)
    profile = models.CharField(max_length=50,default="",unique=True)
    temperature = models.FloatField(null=False)
    log_columndensity = models.FloatField(default=1)
    normalized = ArrayField(models.FloatField(default=1))
    # normalized = models.FloatField(default=1)

class Emission(models.Model):
    molecule = models.CharField(max_length=8,default="")
    isocode = models.IntegerField(null=False,default=1)
    velocity = models.FloatField(null=False)
    thermal = models.FloatField(null=False)
    profile = models.CharField(max_length=50,default="",unique=True)
    temperature = models.FloatField(null=False)
    log_columndensity = models.FloatField(null=False)
    emission = models.FloatField(null=False,default=0)

class Wavelength(models.Model):
    oversampling = models.FloatField(null=False)
    resolution = models.FloatField(null=False)
    wavelength = models.FloatField(null=False,default=0)


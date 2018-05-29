from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    city  = models.CharField(max_length=300)
    state  = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    latitute = models.CharField(max_length=300)
    longitude  = models.CharField(max_length=300)
    photo_url = models.TextField()



class GeoJson(models.Model):
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
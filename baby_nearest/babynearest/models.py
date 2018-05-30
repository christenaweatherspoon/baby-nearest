from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=300, default='')
    url = models.CharField(max_length=300, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    city  = models.CharField(max_length=300, null=True, blank=True)
    state  = models.CharField(max_length=300, db_index=True)
    zipcode = models.CharField(max_length=300, db_index=True)
    latitute = models.CharField(max_length=300, null=True, blank=True)
    longitude  = models.CharField(max_length=300, null=True, blank=True)
    # location = models.ForeignKey(GeoJson, db_index=True)

# class GeoJson(models.Model):
#     name = models.CharField(max_length=300, null=True, blank=True)
#     url = models.CharField(max_length=300, null=True, blank=True)
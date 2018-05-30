from django.shortcuts import render
from rest_framework import generics 
from .serializers import Locationserializer
from .models import Locations

class LocationList(generics.ListCreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = Locationserializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer
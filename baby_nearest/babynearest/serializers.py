from rest_framework import serializers
from .models import Locations

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    locations = serializers.HyperlinkedRelatedField(
        view_name='location-detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Locations
        fields = ('name', 'address', 'city', 'state', 'zipcode', 'longitude', 'latitude')


# class GeoJSON(serializers.HyperlinkedModelSerializer):
#     artist = serializers.HyperlinkedRelatedField(
#         view_name='location-detail',
#         read_only=True
#     )
#     class Meta:
#         model = 
#         fields = ('', '', '', '', 'preview_url',)
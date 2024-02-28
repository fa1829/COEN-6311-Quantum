from rest_framework import serializers
from .models import (Hotels, StatusTypes, RoomTypes, HotelRooms, Airports,
                     AirLines, FlightCategories, TripTypes, Flights,
                     Activities, TravelPackages, Locations, VwTravelPackage)


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'


class StatusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTypes
        fields = '__all__'


class RoomTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTypes
        fields = '__all__'


class HotelRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRooms
        fields = '__all__'


class AirportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = '__all__'


class AirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirLines
        fields = '__all__'


class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'


class FlightDropDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = ['id', 'Flight_Name']


class TripTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripTypes
        fields = '__all__'


class FlightCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightCategories
        fields = '__all__'


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class TravelPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPackages
        fields = '__all__'


class VwTravelPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VwTravelPackage
        fields = '__all__'

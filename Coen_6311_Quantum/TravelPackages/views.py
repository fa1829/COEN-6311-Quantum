from django.shortcuts import render
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import serializers
from .models import (Hotels, StatusTypes, RoomTypes, HotelRooms, Airports,
                     AirLines, FlightCategories, TripTypes, Flights,
                     Activities, TravelPackages, Locations, VwTravelPackage)

from .serializers import (HotelsSerializer, StatusTypesSerializer, RoomTypesSerializer, HotelRoomsSerializer,
                          AirportsSerializer, AirlinesSerializer, FlightCategoriesSerializer, TripTypesSerializer,
                          FlightsSerializer, ActivitiesSerializer,
                          TravelPackagesSerializer, LocationsSerializer, FlightDropDownSerializer,
                          VwTravelPackagesSerializer)


# Locations CRUD
class LocationsListView(APIView):
    serializer_class = LocationsSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            locations = Locations.objects.get(pk=pk)
            serializer = self.serializer_class(locations)

        else:
            # List view logic
            locations = Locations.objects.all()
            serializer = LocationsSerializer(locations, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        locations = Locations.objects.get(pk=pk)
        serializer = self.serializer_class(locations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        locations = Locations.objects.get(pk=pk)
        locations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Status Types CRUD operation class
class StatusTypesListView(APIView):
    serializer_class = StatusTypesSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            status_types = StatusTypes.objects.get(pk=pk)
            serializer = self.serializer_class(status_types)

        else:
            # List view logic
            status_types = StatusTypes.objects.all()
            serializer = StatusTypesSerializer(status_types, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        status_types = StatusTypes.objects.get(pk=pk)
        serializer = self.serializer_class(status_types, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        status_types = StatusTypes.objects.get(pk=pk)
        status_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Room Type CRUD operation class
class RoomTypesListView(APIView):
    serializer_class = RoomTypesSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            room_types = RoomTypes.objects.get(pk=pk)
            serializer = self.serializer_class(room_types)

        else:
            # List view logic
            room_types = RoomTypes.objects.all()
            serializer = RoomTypesSerializer(room_types, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        room_types = RoomTypes.objects.get(pk=pk)
        serializer = self.serializer_class(room_types, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        room_types = RoomTypes.objects.get(pk=pk)
        room_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Hotel CRUD operation class
class HotelsListView(APIView):
    serializer_class = HotelsSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            hotels = Hotels.objects.get(pk=pk)
            serializer = self.serializer_class(hotels)

        else:
            # List view logic
            hotels = Hotels.objects.all()
            serializer = HotelsSerializer(hotels, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        hotels = Hotels.objects.get(pk=pk)
        serializer = self.serializer_class(hotels, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hotels = Hotels.objects.get(pk=pk)
        hotels.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Hotel Room Types CRUD
class HotelRoomsListView(APIView):
    serializer_class = HotelRoomsSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            hotel_rooms = HotelRooms.objects.get(pk=pk)
            serializer = self.serializer_class(hotel_rooms)

        else:
            # List view logic
            hotel_rooms = HotelRooms.objects.all()
            serializer = HotelRoomsSerializer(hotel_rooms, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        hotel_rooms = HotelRooms.objects.get(pk=pk)
        serializer = self.serializer_class(hotel_rooms, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hotel_rooms = HotelRooms.objects.get(pk=pk)
        hotel_rooms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Airport CRUD
class AirportListView(APIView):
    serializer_class = AirportsSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            airports = Airports.objects.get(pk=pk)
            serializer = self.serializer_class(airports)

        else:
            # List view logic
            airports = Airports.objects.all()
            serializer = AirportsSerializer(airports, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        airports = Airports.objects.get(pk=pk)
        serializer = self.serializer_class(airports, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        airports = TravelPackages.objects.get(pk=pk)
        airports.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Airline CRUD
class AirlinesListView(APIView):
    serializer_class = AirlinesSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            airlines = AirLines.objects.get(pk=pk)
            serializer = self.serializer_class(airlines)

        else:
            # List view logic
            airlines = AirLines.objects.all()
            serializer = AirlinesSerializer(airlines, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        airlines = AirLines.objects.get(pk=pk)
        serializer = self.serializer_class(airlines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        airlines = AirLines.objects.get(pk=pk)
        airlines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Flight Categories CRUD
class FlightCategoriesListView(APIView):
    serializer_class = FlightCategoriesSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            flight_categories = FlightCategories.objects.get(pk=pk)
            serializer = self.serializer_class(flight_categories)

        else:
            # List view logic
            flight_categories = FlightCategories.objects.all()
            serializer = FlightCategoriesSerializer(flight_categories, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        flight_categories = FlightCategories.objects.get(pk=pk)
        serializer = self.serializer_class(flight_categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flight_categories = FlightCategories.objects.get(pk=pk)
        flight_categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Flights CRUD
class FlightsListView(APIView):
    serializer_class = FlightsSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            flights = Flights.objects.get(pk=pk)
            serializer = self.serializer_class(flights)

        else:
            # List view logic
            flights = Flights.objects.all()
            serializer = FlightsSerializer(flights, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        flights = Flights.objects.get(pk=pk)
        serializer = self.serializer_class(flights, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flights = Flights.objects.get(pk=pk)
        flights.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Activities CRUD
class ActivitiesListView(APIView):
    serializer_class = ActivitiesSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            activity = Activities.objects.get(pk=pk)
            serializer = self.serializer_class(activity)

        else:
            # List view logic
            activity = Activities.objects.all()
            serializer = ActivitiesSerializer(activity, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        activity = Activities.objects.get(pk=pk)
        serializer = self.serializer_class(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        activity = Activities.objects.get(pk=pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Travel Package CRUD operation
class TravelPackagesListView(APIView):
    serializer_class = TravelPackagesSerializer
    # permission_classes = [IsAuthenticated]
    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            travel_package = TravelPackages.objects.get(pk=pk)
            serializer = self.serializer_class(travel_package)
            return Response(serializer.data)

        else:
            # List view logic
            travel_package = TravelPackages.objects.all()
            serializer = TravelPackagesSerializer(travel_package, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        travel_packages = TravelPackages.objects.get(pk=pk)
        serializer = self.serializer_class(travel_packages, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        travel_package = TravelPackages.objects.get(pk=pk)
        travel_package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlightDropdownViewSet(APIView):
    def get(self, request):
        flightdropdown = Flights.objects.all()
        serializer = FlightDropDownSerializer(flightdropdown, many=True)
        return Response(serializer.data)


class VwTravelPackageViewSet(APIView):
    def get(self, request, pk=None):
        if pk:
            vwpackage = VwTravelPackage.objects.get(pk=pk)
            serializer = VwTravelPackagesSerializer(vwpackage)
            return Response(serializer.data)
        else:
            vwpackage = VwTravelPackage.objects.all()
            serializer = VwTravelPackagesSerializer(vwpackage, many=True)
            return Response(serializer.data)



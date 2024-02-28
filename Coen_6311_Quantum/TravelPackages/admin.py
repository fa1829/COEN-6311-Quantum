# Register your models here.
from django.contrib import admin
from .models import Hotels, StatusTypes, RoomTypes, HotelRooms, Airports, AirLines, FlightCategories, TripTypes, Flights, Locations, Activities, TravelPackages, VwTravelPackage

# Register your models here.

admin.site.register(Hotels)
admin.site.register(StatusTypes)
admin.site.register(RoomTypes)
admin.site.register(HotelRooms)
admin.site.register(Airports)
admin.site.register(AirLines)
admin.site.register(FlightCategories)
admin.site.register(TripTypes)
admin.site.register(Flights)
admin.site.register(Locations)
admin.site.register(Activities)
admin.site.register(TravelPackages)
admin.site.register(VwTravelPackage)

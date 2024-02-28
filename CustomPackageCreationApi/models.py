from django.db import models
from datetime import datetime
from django.utils import timezone
#from django.contrib.auth.models import User
from PackageManagementApi.models import Hotels,StatusTypes,RoomTypes,HotelRooms,Airports,AirLines,FlightCategories,TripTypes,Flights,Locations,Activities,TravelPackages

class CustomPackage(models.Model):
    name = models.CharField(max_length=100)

    hotels = models.ManyToManyField(Hotels)
    hotel_status = models.ManyToManyField(StatusTypes)
    hotel_room_type = models.ManyToManyField(RoomTypes)
    hotel_room_status = models.ForeignKey(HotelRooms, on_delete=models.CASCADE,
                                          related_name='custom_package_hotel_room_status')
    hotel_room_price = models.ForeignKey(HotelRooms, on_delete=models.CASCADE, related_name='custom_package_hotel_room_price')

    airport = models.ManyToManyField(Airports)
    airline = models.ManyToManyField(AirLines)
    flight_category = models.ManyToManyField(FlightCategories)
    trip_type = models.ManyToManyField(TripTypes)
    flight_name_custom_package = models.ForeignKey(Flights, on_delete=models.CASCADE,
                                                   related_name='custom_package_flight_name')
    departure_date = models.DateField(default=datetime.now)
    return_date = models.DateField(default=datetime.now)
    going_to_custom_package = models.ForeignKey(Airports, on_delete=models.CASCADE,
                                                related_name='custom_package_going_to')
    leaving_from_custom_package = models.ForeignKey(Airports, on_delete=models.CASCADE,
                                                    related_name='custom_package_leaving_from')

    location_name_custom_package = models.ManyToManyField(Locations)
    activity_name_custom_package = models.ManyToManyField(Activities)



   # total_price = models.DecimalField(max_digits=10, decimal_places=2)

   # user = models.ForeignKey('auth.User', related_name='tpackages', on_delete=models.CASCADE, null=True)



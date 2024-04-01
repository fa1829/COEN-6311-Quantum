from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User


# Create your models here.


class Hotels(models.Model):
    Hotel_Name = models.CharField(max_length=200, null=True)
    Hotel_Address = models.CharField(max_length=200, null=True)
    Hotel_Phone = models.CharField(max_length=20, null=True)
    Hotel_Email = models.EmailField()
    Hotel_Amenity = models.CharField(max_length=200, null=True)
    Hotel_Rating = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    Hotel_Image = models.CharField(max_length=200, null=True)


class StatusTypes(models.Model):
    Status_Name = models.CharField(max_length=50, null=True)


class RoomTypes(models.Model):
    Type_Name = models.CharField(max_length=200, null=True)


class HotelRooms(models.Model):
    Hotel_ID = ForeignKey(Hotels, on_delete=models.CASCADE, null=True)
    Room_Type_ID = models.ForeignKey(RoomTypes, on_delete=models.CASCADE, null=True)
    Price_Per_Night = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    Room_Status = models.ForeignKey(StatusTypes, on_delete=models.CASCADE, null=True)
    Room_Description = models.CharField(max_length=200, null=True)
    Room_Image = models.CharField(max_length=200, null=True)


class Airports(models.Model):
    Airport_Name = models.CharField(max_length=100, null=True)
    Airport_Address = models.CharField(max_length=100, null=True)
    Airport_Phone = models.CharField(max_length=12,null=True)


class AirLines(models.Model):
    Airline_name = models.CharField(max_length=200, null=True)
    Airline_description = models.CharField(max_length=200, null=True)
    Airline_Image = models.CharField(max_length=200, null=True)


class FlightCategories(models.Model):
    Flight_Category_Name = models.CharField(max_length=50, null=True)
    Flight_Category_Description = models.CharField(max_length=200, null=True)


class TripTypes(models.Model):
    Trip_Type_Name = models.CharField(max_length=50, null=True)
    Trip_Type_Description = models.CharField(max_length=200, null=True)


class Flights(models.Model):
    Flight_Name = models.CharField(max_length=100, null=True)
    Airline_ID = ForeignKey(AirLines, on_delete=models.CASCADE, null=True)
    Flight_Category_ID = models.ForeignKey(FlightCategories, on_delete=models.CASCADE, null=True)
    Flight_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Departure_Date = models.DateTimeField(null=True)
    Rerun_Date = models.DateTimeField(null=True)
    Leaving_from = models.ForeignKey(Airports, on_delete=models.CASCADE, null=True, related_name='leaving_from')
    Going_to = models.ForeignKey(Airports, on_delete=models.CASCADE, null=True, related_name='going_to')


class Locations(models.Model):
    Location_Name = models.CharField(max_length=100, null=True)
    location_Description = models.CharField(max_length=200, null=True)


class Activities(models.Model):
    Activity_Name = models.CharField(max_length=100, null=True)
    Activity_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Activity_Description = models.CharField(max_length=200, null=True)


class TravelPackages(models.Model):
    Travel_Package_Name = models.CharField(max_length=200, null=True)
    Location_ID = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True)
    Flight_ID = models.ForeignKey(Flights, on_delete=models.CASCADE, null=True)
    Hotel_Rooms_ID = models.ForeignKey(HotelRooms, on_delete=models.CASCADE, null=True)
    Activity_ID = models.ForeignKey(Activities, on_delete=models.CASCADE, null=True)
    Package_Price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    Package_Description = models.CharField(max_length=200, null=True)
    Package_Image = models.CharField(max_length=500, null=True)
    user = models.ForeignKey('auth.User', related_name='tpackages', on_delete=models.CASCADE, null=True)


# class CustomTravelPackages(models.Model):
#     Custom_Package_Name = models.CharField(max_length=200, null=True)
#     Location_ID = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True)
#     Flight_ID = models.ForeignKey(Flights, on_delete=models.CASCADE, null=True)
#     Hotel_Rooms_ID = models.ForeignKey(HotelRooms, on_delete=models.CASCADE, null=True)
#     Activity_ID = models.ForeignKey(Activities, on_delete=models.CASCADE, null=True)
#     Package_Price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     Package_Description = models.CharField(max_length=200, null=True)
#     user = models.ForeignKey('auth.User', related_name='cpackages', on_delete=models.CASCADE, null=True)


class VwTravelPackage(models.Model):
    id = models.IntegerField(primary_key=True)
    Travel_Package_Name = models.CharField(max_length=200, null=True)
    Package_Description = models.CharField(max_length=200, null=True)
    Package_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    LocationID = models.IntegerField(null=True)
    Location_Name = models.CharField(max_length=200, null=True)
    FlightID = models.IntegerField(null=True)
    Flight_Name = models.CharField(max_length=200, null=True)
    HotelRoomID = models.IntegerField(null=True)
    HotelRoom = models.CharField(max_length=200, null=True)
    ActivityID = models.IntegerField(null=True)
    Activity_Name = models.CharField(max_length=200, null=True)
    AirlineID = models.IntegerField(null=True)
    Airline_name = models.CharField(max_length=200, null=True)
    Room_Image = models.CharField(max_length=200, null=True)
    Package_Image = models.CharField(max_length=500, null=True)

    class Meta:
        managed = False
        db_table = 'vw_TravelPackage'


# class PaymentInfo(models.Model):
#     Travel_Package_ID = models.ForeignKey(TravelPackages, on_delete=models.CASCADE, null=True)
#     Customer_ID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     Payment = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     Payment_Date = models.DateField(null=True)


class BookingInfo(models.Model):
    Package_ID = models.ForeignKey(TravelPackages, on_delete=models.CASCADE, null=True)
    Customer_ID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Card_Number = models.IntegerField(null=True)
    Expiry_Date = models.CharField(max_length=8, null=True)
    CVC_Number = models.IntegerField(null=True)
    Payment_Amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Booking_Date = models.DateTimeField(null=True)

















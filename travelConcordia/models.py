# travel/models.py
from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    airline = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=50)
    arrival_airport = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration_hours = models.PositiveIntegerField()
    flight_price_cad = models.DecimalField(max_digits=10, decimal_places=2)
    # other flight-related attributes

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50)
    price_per_night_cad = models.DecimalField(max_digits=10, decimal_places=2)
    # other hotel-related attributes

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_hours = models.PositiveIntegerField()
    price_cad = models.DecimalField(max_digits=10, decimal_places=2)
    # other activity-related attributes

class TravelPackage(models.Model):
    name = models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight)
    hotels = models.ManyToManyField(Hotel)
    activities = models.ManyToManyField(Activity)
    total_cost_cad = models.DecimalField(max_digits=10, decimal_places=2)
    # other package-related attributes

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other customer-related attributes

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    travel_package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)  # True if payment is completed
    booking_date = models.DateTimeField(auto_now_add=True)
    # other booking-related attributes

class Agent(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="id")

    def __str__(self):
        return self.username
class Report(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    revenue_cad = models.DecimalField(max_digits=10, decimal_places=2)
    booking_count = models.PositiveIntegerField()
    # other report-related attributes

class Notification(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.TextField()
    sent_datetime = models.DateTimeField(auto_now_add=True)
    # other notification-related attributes

class CustomPackage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flights = models.ManyToManyField(Flight)
    hotels = models.ManyToManyField(Hotel)
    activities = models.ManyToManyField(Activity)
    total_cost_cad = models.DecimalField(max_digits=10, decimal_places=2)
    # other custom package-related attributes

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_cad = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

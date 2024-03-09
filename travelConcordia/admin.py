from django.contrib import admin
from .models import Flight, Hotel, Activity, TravelPackage, Customer, Booking, Agent, Report, Notification, \
    CustomPackage, Payment

# Register your models here.
register_models = [Flight, Hotel, Activity, TravelPackage, Customer, Booking, Agent, Report, Notification, CustomPackage,Payment]
admin.site.register(register_models)
# Path: serializers.py
# Compare this snippet from tests.py:
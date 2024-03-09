# travelConcordia/urls.py
from django.urls import path
from .views import (
    FlightListCreateView, HotelListCreateView, ActivityListCreateView, TravelPackageListCreateView,
    CustomerListCreateView, BookingListView, AgentCreateView, ReportListCreateView,
    NotificationListCreateView, CustomPackageListCreateView, AgentListView, PaymentView
)

urlpatterns = [
    path('flights/', FlightListCreateView.as_view(), name='flight-list-create'),
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('packages/', TravelPackageListCreateView.as_view(), name='package-list-create'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('agents/', AgentListView.as_view(), name='agent-list'),
    path('agents/create/', AgentCreateView.as_view(), name='agent-create'),
    path('reports/', ReportListCreateView.as_view(), name='report-list-create'),
    path('notifications/', NotificationListCreateView.as_view(), name='notification-list-create'),
    path('custom-packages/', CustomPackageListCreateView.as_view(), name='custom-package-list-create'),
    path('payment/', PaymentView.as_view(), name='process-payment'),
]


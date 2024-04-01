from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (StatusTypesListView, RoomTypesListView, HotelsListView,
                    TravelPackagesListView, HotelRoomsListView, AirportListView, AirlinesListView,
                    FlightsListView, FlightCategoriesListView, ActivitiesListView, LocationsListView,
                    FlightDropdownViewSet, VwTravelPackageViewSet, BookingInfoListView)


urlpatterns = [
    path('statustypes/', StatusTypesListView.as_view()),
    path('statustypes/<int:pk>/', StatusTypesListView.as_view()),
    path('roomtypes/', RoomTypesListView.as_view()),
    path('roomtypes/<int:pk>/', RoomTypesListView.as_view()),
    path('hotels/', HotelsListView.as_view()),
    path('hotels/<int:pk>/', HotelsListView.as_view()),
    path('travelpackages/', TravelPackagesListView.as_view()),
    path('travelpackages/<int:pk>/', TravelPackagesListView.as_view()),
    path('bookinginfo/', BookingInfoListView.as_view()),
    path('bookinginfo/<int:pk>/', BookingInfoListView.as_view()),
    path('hotelsrooms/', HotelRoomsListView.as_view()),
    path('hotelsrooms/<int:pk>/', HotelRoomsListView.as_view()),
    path('airport/', AirportListView.as_view()),
    path('airport/<int:pk>/', AirportListView.as_view()),
    path('airlines/', AirlinesListView.as_view()),
    path('airlines/<int:pk>/', AirlinesListView.as_view()),
    path('flights/', FlightsListView.as_view()),
    path('flights/<int:pk>/', FlightsListView.as_view()),
    path('flightcategories/', FlightCategoriesListView.as_view()),
    path('flightcategories/<int:pk>/', FlightCategoriesListView.as_view()),
    path('activities/', ActivitiesListView.as_view()),
    path('activities/<int:pk>/', ActivitiesListView.as_view()),
    path('locations/', LocationsListView.as_view()),
    path('locations/<int:pk>/', LocationsListView.as_view()),
    path('flightdropdown/', FlightDropdownViewSet.as_view()),
    path('flightdropdown/<int:pk>', FlightDropdownViewSet.as_view()),
    path('vwtravelpackages/', VwTravelPackageViewSet.as_view()),
    path('vwtravelpackages/<int:pk>/', VwTravelPackageViewSet.as_view()),


]

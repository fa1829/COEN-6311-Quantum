# travelConcordia/views.py
from django.conf import settings  # Add this import statement
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Flight, Hotel, Activity, TravelPackage, Customer, Booking, Agent, Report, Notification, CustomPackage
from .serializers import (
    FlightSerializer, HotelSerializer, ActivitySerializer, TravelPackageSerializer,
    CustomerSerializer, BookingSerializer, AgentSerializer, ReportSerializer, NotificationSerializer, CustomPackageSerializer, PaymentSerializer
)

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import stripe

# Set the Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed

class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    pagination_class = CustomPageNumberPagination

class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = CustomPageNumberPagination

class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = CustomPageNumberPagination

class TravelPackageListCreateView(generics.ListCreateAPIView):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer
    pagination_class = CustomPageNumberPagination

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomPageNumberPagination

class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgentListView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgentCreateView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    pagination_class = CustomPageNumberPagination

class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = CustomPageNumberPagination

class CustomPackageListCreateView(generics.ListCreateAPIView):
    queryset = CustomPackage.objects.all()
    serializer_class = CustomPackageSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        # Set the customer for the custom package based on the authenticated user
        serializer.save(customer=self.request.user.customer)

class PaymentView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Retrieve user and payment information from the request
            user = request.user
            amount = request.data.get('amount')

            # Create a Stripe PaymentIntent
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Stripe requires the amount in cents
                currency='CAD',
            )

            # Create a record of the payment in your database
            payment_data = {
                'user': user,
                'amount': amount,
            }
            payment_serializer = PaymentSerializer(data=payment_data)
            payment_serializer.is_valid(raise_exception=True)
            payment_serializer.save()

            return Response({'client_secret': payment_intent.client_secret})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

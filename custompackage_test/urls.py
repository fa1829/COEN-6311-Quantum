from django.urls import path, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomPackageListView



urlpatterns = [
    path('custompackage/', CustomPackageListView.as_view()),
    path('custompackage/<int:pk>/', CustomPackageListView.as_view())

]
from rest_framework import serializers
from .models import CustomPackage

class CustomPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPackage
        fields = '__all__'

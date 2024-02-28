#from django.shortcuts import render
from django.http import Http404
#from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import serializers
from .models import CustomPackage

from .serializers import CustomPackageSerializer


# Custom Package CRUD operation
class CustomPackageListView(APIView):
    serializer_class = CustomPackageSerializer
    def get(self, request, pk=None, format=None):
        if pk:
            # Detail view logic
            custom_package = CustomPackage.objects.get(pk=pk)
            serializer = self.serializer_class(custom_package)

        else:
            # List view logic
            custom_package = CustomPackage.objects.all()
            serializer = CustomPackageSerializer(custom_package, many=True)

            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        custom_package = CustomPackage.objects.get(pk=pk)
        serializer = self.serializer_class(custom_package, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        custom_package = CustomPackage.objects.get(pk=pk)
        custom_package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

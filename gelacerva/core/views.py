from django.shortcuts import render
from rest_framework import generics

from core.models import *
from core.serializers import *

class DeviceCreateView(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DeviceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new device."""
        serializer.save()


class TemperatureCreateView(generics.ListCreateAPIView):
    queryset = Temperatures.objects.all()
    serializer_class = TemperatureSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new temperature."""
        serializer.save()

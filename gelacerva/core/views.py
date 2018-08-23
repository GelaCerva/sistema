from core.models import *
from core.serializers import *

from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response


class DeviceCreateView(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DeviceSerializer

class TemperatureCreateView(generics.ListCreateAPIView):
    queryset = Temperatures.objects.all()
    serializer_class = TemperatureSerializer

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        try:
            device = Devices.objects.get(pk=request.data["device"])
            configs = device.get_device_configs()
        except:
            return Response()
        return Response(configs)

from rest_framework import serializers
from core.models import Temperatures, Devices

class TemperatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperatures
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Devices
        fields = "__all__"

from django.db import models
from django.contrib.auth.models import User


class Devices(models.Model):
    device_mac = models.CharField(null=False, blank=False, default="", max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(null=False, blank=False, default="", max_length=5000)

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"

class Temperatures(models.Model):
    temperature = models.FloatField(null=False, blank=False, default=0.00)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "temperatures"
        verbose_name_plural = "temperatures"

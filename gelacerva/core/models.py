from django.db import models
from django.contrib.auth.models import User


class Devices(models.Model):
    device_mac = models.CharField(null=False, blank=False, default="", max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(null=False, blank=False, default="", max_length=5000)

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"

    def __str__(self):
        return "Dispositivo: " + self.device_mac

class Temperatures(models.Model):
    temperature = models.FloatField(null=False, blank=False, default=0.00)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "temperatures"
        verbose_name_plural = "temperatures"

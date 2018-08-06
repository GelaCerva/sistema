from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Devices(models.Model):
    device_mac = models.CharField(null=False, blank=False, default="")
    user = models.ForeignKey(User)
    description = models.CharField(null=False, blank=False, default="")

class Temperatures(models.Model):
    temperature = models.FloatField(null=False, blank=False, default=0.00)
    device = models.ForeignKey(Devices)

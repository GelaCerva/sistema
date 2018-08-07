from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from statistics import mean

class Devices(models.Model):
    device_mac = models.CharField(null=False, blank=False, default="", max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(null=False, blank=False, default="", max_length=5000)

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"

    def __str__(self):
        return "Dispositivo: " + self.device_mac


class TempObj():
    def __init__(self, temp, date, devpk):
        self.temp = temp
        self.date = date
        self.devpk = devpk


class Temperatures(models.Model):
    temperature = models.FloatField(null=False, blank=False, default=0.00)
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "temperatures"
        verbose_name_plural = "temperatures"

    def return_first_dev_obj(time_delta):
        a_week_ago = datetime.now().date() - timedelta(days=time_delta)
        today_plus_one = datetime.now().date() + timedelta(days=1)
        temps_objs = Temperatures.objects.filter(date__gte=a_week_ago, date__lt=today_plus_one, device=1)
        values = [(obj.temperature, str(obj.date.date())) for obj in temps_objs]
        vs = {}
        for v in values:
            temp, date = v
            date = str(date)
            if date in vs:
                vs[date].append(temp)
            else:
                vs[date] = []
                vs[date].append(temp)

        mean_temps = []

        for temps in vs.values():
            mean_temps.append(mean(temps))

        return mean_temps, [date for date in vs.keys()]


    def return_temp_objs_devs(time_delta):
        a_week_ago = datetime.now().date() - timedelta(days=time_delta)
        today_plus_one = datetime.now().date() + timedelta(days=1)
        
        devs_temps = []

        for dev in Devices.objects.all():
            temps_objs = Temperatures.objects.filter(date__gte=a_week_ago, date__lt=today_plus_one, device=dev.pk)
            values = [(obj.temperature, str(obj.date.date())) for obj in temps_objs]

            vs = {}
            for v in values:
                temp, date = v
                date = str(date)
                if date in vs:
                    vs[date].append(temp)
                else:
                    vs[date] = []
                    vs[date].append(temp)

            mean_temps = []

            for temps in vs.values():
                devs_temps.append(TempObj(mean(temps), date, dev.pk))
            
        return devs_temps
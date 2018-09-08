from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from statistics import mean

class Devices(models.Model):
    device_mac = models.CharField(null=False, blank=False, default="", max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(null=False, blank=False, default="", max_length=5000)
    set_point = models.FloatField(null=False, blank=False, default=0)
    max_temp = models.FloatField(null=False, blank=False, default=0)
    min_temp = models.FloatField(null=False, blank=False, default=0)
    bandwith = models.FloatField(null=False, blank=False, default=0)
    control_type = models.BooleanField(null=False, blank=False, default=0)
    sm_mode = models.BooleanField(null=False, blank=False, default=0)
    relay_state = models.BooleanField(null=False, blank=False, default=0)
    temp_variation = models.FloatField(null=False, blank=False, default=0)

    class Meta:
        verbose_name = "device"
        verbose_name_plural = "devices"

    def __str__(self):
        return "Dispositivo: " + self.device_mac

    def get_device_configs(self):
        return {
            "set_point": self.set_point,
            "max_temp": self.set_point + self.temp_variation,
            "min_temp": self.set_point - self.temp_variation
        }

    def get_last_temperature(self):
        try:
            temps = Temperatures.objects.filter(device__pk=self.pk).order_by('-pk')
            return temps[0].temperature
        except:
            return None

class TempObj():
    def __init__(self, temp, date, devpk):
        self.temp = temp
        self.date = date
        self.devpk = devpk


class Temperatures(models.Model):

    # TODO colocar um json field para pegar a HTTP request do device
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

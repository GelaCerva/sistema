from core.forms import DeviceForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from statistics import mean
from datetime import timedelta, datetime
from django.utils import timezone
import json

from django.contrib.auth import logout
from core.models import *

from core.models import *

@login_required
def index(request):
    context = {}
    temps_graph, dates_graph = Temperatures.return_first_dev_obj(7)
    context["temps_graph"] = json.dumps(temps_graph)
    context["dates_graph"] = json.dumps(dates_graph)
    context["temps"] = Temperatures.return_temp_objs_devs(7)
    context["devices"] = Devices.objects.all()
    context["title"] = "Dashboard - Última Semana"

    return render(request, template_name="dashboard/index.html", context=context)

@login_required
def report_days(request, days):
    context = {}
    temps_graph, dates_graph = Temperatures.return_first_dev_obj(days)
    context["temps_graph"] = json.dumps(temps_graph)
    context["dates_graph"] = json.dumps(dates_graph)
    context["temps"] = Temperatures.return_temp_objs_devs(days)
    context["devices"] = Devices.objects.all()
    context["title"] = "Dashboard - {} dias".format(days)

    return render(request, template_name="dashboard/index.html", context=context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def devices_list(request):
    context = {}
    context["devices"] = Devices.objects.all()
    devs = len(context["devices"])
    context["title"] = "Listagem - {} Dispostivos".format(devs)
    return render(request, template_name="dashboard/devices.html", context=context)

@login_required
def device_edit(request, pk):
    context = {}
    context["device"] = Devices.objects.get(pk=pk)
    context["form"] = DeviceForm(request.POST or None, instance=context["device"])
    if request.method == "POST":
        if context["form"].is_valid():
            context["form"].save()
            import ipdb; ipdb.set_trace()
            return redirect('/devices/')
        else:
            context["error"] = "Erro"
    context["form"] = DeviceForm(instance=context["device"] or None)

    return render(request, template_name="dashboard/device_edit.html", context=context)

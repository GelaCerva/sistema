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

    return render(request, template_name="dashboard/index.html", context=context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
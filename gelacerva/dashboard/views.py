from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from datetime import timedelta, datetime
from django.utils import timezone
# Create your views here.

from core.models import *

@login_required
def index(request):
    a_week_ago = datetime.now().date() - timedelta(days=7)
    today_plus_one = datetime.now().date() + timedelta(days=1)
    context = {}
    context["temps"] = Temperatures.objects.filter(date__gte=a_week_ago, date__lt=today_plus_one)
    context["temps"].group_by('device')
    # context["temps"].annotate(mean_temperature=Avg('temperature'))

    return render(request, template_name="dashboard/index.html", context=context)

"""gelacerva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from core.views import *
import dashboard.views as d_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/temp/', TemperatureCreateView.as_view()),
    path('api/dev/', DeviceCreateView.as_view()),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout/', d_views.logout_view, name="logout"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('report/<int:days>/', d_views.report_days, name="report"),
    path('devices/', d_views.devices_list, name="devices_list"),
    path('device/<int:pk>', d_views.device_edit, name="device_edit"),
    path('', d_views.index, name="home")

]

from core.models import Devices
from django.forms import ModelForm

class DeviceForm(ModelForm):
    class Meta:
        model = Devices
        fields = [
            "device_mac",
            "description",
            "set_point",
            "temp_variation",
            "user",
            "bandwith",
            "control_type",
            "sm_mode",
            "relay_state"
        ]

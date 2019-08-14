from django.forms import ModelForm
from .models import Clock

class ClockForm(ModelForm):
    class Meta:
        model = Clock
        fields = ("name", "description", "clock_type", "following_clock")

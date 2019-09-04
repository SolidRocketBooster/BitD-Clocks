from django import forms
from .models import Clock

class ClockForm(forms.ModelForm):
    class Meta:
        model = Clock
        fields = ("title", "description", 'clock_type', "clock_length", "compleation" , "following_clock")
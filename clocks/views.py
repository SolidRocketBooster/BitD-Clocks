from django.shortcuts import render, get_list_or_404
from .models import Clock
from .forms import ClockForm

def ClocksView(request):
    return render(request, 'clocks\clocks.html', {'clocks': Clock.objects.all()})

def post_new(request):
    form = ClockForm()
    return render(request, 'clocks\edit_clock.html', {'form': form})

# Create your views here.

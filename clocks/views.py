from django.shortcuts import render, get_list_or_404
from .models import Clock

def ClocksView(request):
    return render(request, 'clocks\clocks.html', {'clocks': Clock.objects.all()})

# Create your views here.

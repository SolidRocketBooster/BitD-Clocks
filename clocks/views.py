from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import Clock
from .forms import ClockForm

def ClocksView(request):
    clocks = Clock.objects.all()
    return render(request, 'clocks\clocks_list.html', {'clocks': clocks})

def postNew(request):
    if request.method == "POST":
        form = ClockForm(request.POST)
        if form.is_valid():
            clock = form.save(commit=False)
            clock.save()
            return redirect('clocks_list')
    else:
        form = ClockForm()
    return render(request, 'clocks\edit_clock.html', {'form': form})

def clockEdit(request, pk):
    clock = get_object_or_404(Clock, pk=pk)
    if request.method == "POST":
        form = ClockForm(request.POST, instance=clock)
        if form.is_valid():
            clock = form.save(commit=False)
            clock.save()
            return redirect('clocks_list')
    else:
        form = ClockForm(instance=clock)
    return render(request, 'clocks\edit_clock.html', {'form': form, 'clock': clock})

def clockDelete(request, pk):
    clock = get_object_or_404(Clock, pk=pk)
    clock.delete()
    return redirect('clocks_list')

def clockUp(request, pk):
    clock = get_object_or_404(Clock, pk=pk)
    clock.increase()
    return redirect('clocks_list')

def clockDown(request, pk):
    clock = get_object_or_404(Clock, pk=pk)
    clock.decrease()
    return redirect('clocks_list')


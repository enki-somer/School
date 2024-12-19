from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from .forms import ScheduleForm

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'teachers/schedule_list.html', {'schedules': schedules})

def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'teachers/schedule_form.html', {'form': form})

def schedule_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'teachers/schedule_form.html', {'form': form})

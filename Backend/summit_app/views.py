from django.shortcuts import render
from .models import Schedule
from django.db.models import DateField

def schedule_view(request):
    schedules = Schedule.objects.all().order_by('day', 'start_time')
    grouped_schedules = {}
    
    for schedule in schedules:
        if schedule.day not in grouped_schedules:
            grouped_schedules[schedule.day] = []
        grouped_schedules[schedule.day].append(schedule)
    
    return render(request, 'schedule.html', {'grouped_schedules': grouped_schedules})
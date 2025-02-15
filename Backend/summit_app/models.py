from django.db import models

class Schedule(models.Model):
    day = models.DateField()  # The date of the event
    start_time = models.TimeField()  # Start time
    end_time = models.TimeField()  # End time
    plan_detail = models.TextField()  # Description of the event

    def __str__(self):
        return f"{self.day.strftime('%A, %B %d')} - {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"
    
    class Meta:
        ordering = ['day', 'start_time']  # Sort by date and then by start time
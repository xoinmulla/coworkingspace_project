from django.db import models
from django.contrib.auth.models import User
from spaces.models import Space

BOOKING_STATUS = (
    ('booked', 'Booked'),
    ('cancelled', 'Cancelled'),
    ('rescheduled', 'Rescheduled'),
)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    booking_date = models.DateField()
    time_slot = models.CharField(max_length=50)  # e.g., "09:00-12:00"
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='booked')

    def __str__(self):
        return f"{self.user.username} - {self.space.name} on {self.booking_date}"

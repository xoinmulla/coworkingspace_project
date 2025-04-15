from django.shortcuts import render, redirect, get_object_or_404
from spaces.models import Space
from .models import Booking
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def book_space(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        time_slot = request.POST.get('time_slot')
        Booking.objects.create(
            user=request.user,
            space=space,
            booking_date=booking_date,
            time_slot=time_slot,
            status='booked'
        )
        # Redirect to a confirmation page or booking list.
        return redirect('booking-list')
    return render(request, 'bookings/booking_form.html', {'space': space, 'today': date.today()})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

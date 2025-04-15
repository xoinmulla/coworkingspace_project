from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from spaces.models import Space
from bookings.models import Booking
from reviews.models import Review
from payments.models import Payment

# Dashboard overview
@staff_member_required
def dashboard(request):
    total_spaces = Space.objects.count()
    total_bookings = Booking.objects.count()
    total_payments = Payment.objects.filter(status='completed').count()
    total_reviews = Review.objects.count()
    context = {
        'total_spaces': total_spaces,
        'total_bookings': total_bookings,
        'total_payments': total_payments,
        'total_reviews': total_reviews,
    }
    return render(request, 'adminpanel/dashboard.html', context)

# Space management view (list spaces with admin options)
@staff_member_required
def space_management(request):
    spaces = Space.objects.all()
    return render(request, 'adminpanel/space_management.html', {'spaces': spaces})

# Booking management view
@staff_member_required
def booking_management(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'adminpanel/booking_management.html', {'bookings': bookings})

# Reporting view (a simple representation of reports)
@staff_member_required
def reporting(request):
    # For demonstration, we simply show counts and leave charting to future iterations.
    report = {
        'space_utilization': Booking.objects.count(),
        'revenue': Payment.objects.filter(status='completed').count() * 50,  # assuming fixed amount
        'feedback_count': Review.objects.count(),
    }
    return render(request, 'adminpanel/reporting.html', {'report': report})

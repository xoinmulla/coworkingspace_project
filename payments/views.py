from django.shortcuts import render, redirect, get_object_or_404
from bookings.models import Booking
from .models import Payment

def process_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        # In a real-world scenario, here you would integrate with a payment gateway.
        # For simulation, we assume payment is successful.
        payment, created = Payment.objects.get_or_create(booking=booking, defaults={'amount': 50.00})
        payment.status = 'completed'
        payment.transaction_id = 'SIMULATEDTXN12345'
        payment.save()
        return render(request, 'payments/payment_success.html', {'payment': payment})
    return render(request, 'payments/payment_form.html', {'booking': booking})

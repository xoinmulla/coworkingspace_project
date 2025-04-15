from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='admin-dashboard'),
    path('spaces/', views.space_management, name='space-management'),
    path('bookings/', views.booking_management, name='booking-management'),
    path('reporting/', views.reporting, name='reporting'),
]

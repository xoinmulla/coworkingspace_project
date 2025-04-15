from django.urls import path
from . import views

urlpatterns = [
    path('process/<int:booking_id>/', views.process_payment, name='process-payment'),
]

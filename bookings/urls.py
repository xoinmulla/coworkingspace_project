from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:space_id>/', views.book_space, name='book-space'),
    path('my-bookings/', views.booking_list, name='booking-list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.space_list, name='space-list'),
    path('<int:space_id>/', views.space_detail, name='space-detail'),
]

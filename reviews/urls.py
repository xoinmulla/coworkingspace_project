from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='review-index'),  # New pattern for /reviews/
    path('add/<int:space_id>/', views.add_review, name='add-review'),
    path('<int:space_id>/', views.list_reviews, name='list-reviews'),
]

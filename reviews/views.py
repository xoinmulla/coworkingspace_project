from django.shortcuts import render, get_object_or_404
from .models import Review

def index(request):
    # List all reviews (or adjust as needed for your use case)
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/index.html', {'reviews': reviews})

def add_review(request, space_id):
    # existing add_review view implementation
    # Your code here...
    pass

def list_reviews(request, space_id):
    # existing list_reviews view implementation
    # Your code here...
    pass

# In your views.py
# In your views.py
def index(request):
    reviews = Review.objects.all()
    for review in reviews:
        review.full_stars = range(review.rating)  # Filled stars
        review.empty_stars = range(5 - review.rating)  # Empty stars
    return render(request, 'reviews/index.html', {'reviews': reviews})


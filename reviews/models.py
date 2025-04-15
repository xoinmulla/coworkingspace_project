from django.db import models
from django.contrib.auth.models import User
from spaces.models import Space

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # e.g., 1-5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.space.name}"

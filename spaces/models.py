from django.db import models

class Space(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=300)
    available = models.BooleanField(default=True)
    pricing = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

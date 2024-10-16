# rentals/models.py
from django.db import models

class Equipment(models.Model):
    CATEGORY_CHOICES = [
        ('camera', 'Camera'),
        ('lighting', 'Lighting'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    days = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_amount = self.equipment.price_per_day * self.days
        super().save(*args, **kwargs)

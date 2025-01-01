from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

class Jewelry(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('AUCTIONING', 'Auctioning'),
        ('SOLD', 'Sold'),
        ('DELIVERED', 'Delivered'),
        ('NO_BIDS','No Bids')
    )

    jewelry_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jewelries')
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_1 = models.ImageField(upload_to='jewelry/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='jewelry/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='jewelry/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    preliminary_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Thêm dòng này
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Thêm dòng này
    received_at = models.DateTimeField(null=True, blank=True) # Thêm dòng này
    seller_approved = models.BooleanField(default=False) # Thêm dòng này

    def __str__(self):
        return self.name

    def clean(self):
        if self.initial_price is not None and self.initial_price <= 0:
            raise ValidationError({'initial_price': 'Initial price must be greater than zero.'})
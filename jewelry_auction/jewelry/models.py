from django.db import models
from users.models import User

class Jewelry(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('AUCTIONING', 'Auctioning'),
        ('SOLD', 'Sold'),
        ('DELIVERED', 'Delivered'),
    )

    jewelry_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jewelries')
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_1 = models.ImageField(upload_to='jewelry/')
    image_2 = models.ImageField(upload_to='jewelry/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='jewelry/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
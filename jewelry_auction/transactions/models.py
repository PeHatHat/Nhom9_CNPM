from django.db import models
from users.models import User
from auctions.models import Auction
from django.core.exceptions import ValidationError

class Transaction(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )

    transaction_id = models.AutoField(primary_key=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="transactions")
    winning_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_transactions', null=True, blank=True)
    jewelry_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sold_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Transaction {self.transaction_id} for {self.auction}"
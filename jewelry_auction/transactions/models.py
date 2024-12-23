from django.db import models
from users.models import User
from auctions.models import Auction

class Transaction(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )

    transaction_id = models.AutoField(primary_key=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    winning_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='won_transactions')
    jewelry_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sold_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Transaction {self.transaction_id} for {self.auction}"

    def save(self, *args, **kwargs):
        if self.pk is None:  # Chỉ tính toán khi tạo mới
            if self.auction and self.auction.status == 'CLOSED':
                highest_bid = self.auction.bids.order_by('-amount').first()
                if highest_bid:
                    from core.models import FeeConfiguration
                    fee_config = FeeConfiguration.objects.first()
                    if fee_config:
                        self.amount = highest_bid.amount
                        self.fee = self.amount * fee_config.fee_rate
        super(Transaction, self).save(*args, **kwargs)
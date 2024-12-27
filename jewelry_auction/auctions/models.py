from django.db import models
from users.models import User
from jewelry.models import Jewelry
from django.utils import timezone
from django.apps import apps
from django.core.exceptions import ValidationError

class Auction(models.Model):
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('CANCELED', 'Canceled'),
    )

    auction_id = models.AutoField(primary_key=True)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_auctions')
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_auctions')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')
    winning_bid = models.ForeignKey('bids.Bid', on_delete=models.SET_NULL, null=True, blank=True, related_name='won_auction')

    def __str__(self):
        return f"Auction {self.auction_id} for {self.jewelry.name}"

    def is_open(self):
        return self.status == 'OPEN'

    def close_auction(self):
        if self.status == 'OPEN' and self.end_time <= timezone.now():
            self.status = 'CLOSED'
            highest_bid = self.bids.order_by('-amount').first()

            if highest_bid:
                self.winning_bid = highest_bid

                # Cập nhật trạng thái của jewelry
                jewelry = self.jewelry
                jewelry.status = 'SOLD'

                # Chuyển JCoin
                highest_bid.user.jcoin_balance -= highest_bid.amount
                highest_bid.user.save()

                jewelry.owner.jcoin_balance += highest_bid.amount
                jewelry.owner.save()
            else:
                # Nếu không có bid nào, cập nhật trạng thái jewelry về 'APPROVED'
                jewelry = self.jewelry
                jewelry.status = 'APPROVED'
            
            jewelry.save()
            self.save()
    
    def save(self, *args, **kwargs):
        # Kiểm tra và cập nhật trạng thái của phiên đấu giá
        if self.status == 'OPEN' and self.end_time <= timezone.now():
            self.close_auction()
        super(Auction, self).save(*args, **kwargs)
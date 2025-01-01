from django.db import models
from users.models import User
from django.core.exceptions import ValidationError
from django.db.models import Max

class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    auction = models.ForeignKey('auctions.Auction', on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid {self.bid_id} by {self.user.username} on {self.auction}"

    def clean(self):
        # Kiểm tra nếu người dùng đang cố gắng đặt giá thầu cho chính mình
        if self.user == self.auction.jewelry.owner:
            raise ValidationError("You cannot bid on your own jewelry.")

        # Kiểm tra nếu giá thầu thấp hơn giá khởi điểm
        if self.auction.jewelry.initial_price is None:
          raise ValidationError("Initial Price is not set yet")

        if self.amount < self.auction.jewelry.initial_price:
            raise ValidationError("Bid amount must be greater than or equal to the initial price.")

        # Kiểm tra nếu giá thầu thấp hơn giá thầu cao nhất hiện tại
        highest_bid = Bid.objects.filter(auction=self.auction).aggregate(Max('amount'))['amount__max']
        if highest_bid is not None and self.amount <= highest_bid:
            raise ValidationError("Bid amount must be greater than the current highest bid.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Bid, self).save(*args, **kwargs)
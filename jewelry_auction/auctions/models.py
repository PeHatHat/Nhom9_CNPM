from django.db import models
from users.models import User
from jewelry.models import Jewelry
from django.utils import timezone

class Auction(models.Model):
    """
    Model representing an auction session.

    Fields:
        - auction_id: Primary key.
        - jewelry: The jewelry being auctioned (ForeignKey to Jewelry).
        - manager: User managing the auction (ForeignKey to User, optional).
        - staff: Staff assigned to the auction (ForeignKey to User, optional).
        - start_time: Auction start time.
        - end_time: Auction end time.
        - status: Current status of the auction (Created, Open, Closed, Canceled).
    """
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
                self.save()

                # Cập nhật trạng thái của jewelry
                jewelry = self.jewelry
                jewelry.status = 'SOLD'
                jewelry.save()

                # Tạo Transaction (nếu đấu giá thành công)
                from transactions.models import Transaction
                from core.models import FeeConfiguration

                fee_rate = FeeConfiguration.objects.first().fee_rate
                transaction_amount = highest_bid.amount
                fee = transaction_amount * fee_rate

                transaction = Transaction.objects.create(
                    auction=self,
                    winning_bidder=highest_bid.user,
                    jewelry_owner=jewelry.owner,
                    amount=transaction_amount,
                    fee=fee,
                    status='COMPLETED'
                )

                # Chuyển JCoin
                highest_bid.user.jcoin_balance -= transaction_amount
                highest_bid.user.save()

                jewelry.owner.jcoin_balance += (transaction_amount - fee)
                jewelry.owner.save()
            else:
                # Nếu không có bid nào, cập nhật trạng thái jewelry về 'APPROVED'
                jewelry = self.jewelry
                jewelry.status = 'APPROVED'
                jewelry.save()
from django.db import models
from users.models import User
from jewelry.models import Jewelry
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import F
from core.models import FeeConfiguration
from notifications.models import Notification

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
    winning_bid = models.OneToOneField('bids.Bid', on_delete=models.SET_NULL, null=True, blank=True, related_name="won_auction")

    def __str__(self):
        return f"Auction {self.auction_id} for {self.jewelry.name}"

    def is_open(self):
        return self.status == 'OPEN'

    def open_auction(self):
        if self.status == 'CREATED' and self.start_time <= timezone.now():
            self.status = 'OPEN'
            self.save()

    def close_auction(self):
        from bids.models import Bid
        if self.status == 'OPEN' and self.end_time <= timezone.now():
            self.status = 'CLOSED'
            highest_bid = self.bids.order_by('-amount').first()

            if highest_bid:
                self.winning_bid = highest_bid
                self.save()

                # Cập nhật trạng thái của jewelry
                auction_jewelry = self.jewelry
                auction_jewelry.status = 'SOLD'
                auction_jewelry.save()

                # Tạo Transaction (nếu đấu giá thành công)
                fee_config = FeeConfiguration.objects.first()
                if fee_config:
                    transaction_amount = highest_bid.amount
                    fee = transaction_amount * fee_config.fee_rate

                    # Sử dụng string literal 'transactions.Transaction'
                    Transaction = models.get_model('transactions', 'Transaction')
                    transaction = Transaction.objects.create(
                        auction=self,
                        winning_bidder=highest_bid.user,
                        jewelry_owner=auction_jewelry.owner,
                        amount=transaction_amount,
                        fee=fee,
                        status='COMPLETED'
                    )

                    # Chuyển JCoin với F expressions
                    highest_bid.user.jcoin_balance = F('jcoin_balance') - transaction_amount
                    highest_bid.user.save()

                    auction_jewelry.owner.jcoin_balance = F('jcoin_balance') + (transaction_amount - fee)
                    auction_jewelry.owner.save()

                    # Tạo thông báo cho người thắng cuộc
                    Notification.objects.create(
                        user=highest_bid.user,
                        message=f"Chúc mừng! Bạn đã thắng đấu giá trang sức '{auction_jewelry.name}' với giá {highest_bid.amount} JCoins."
                    )

                    # Tạo thông báo cho người bán
                    Notification.objects.create(
                        user=auction_jewelry.owner,
                        message=f"Trang sức '{auction_jewelry.name}' của bạn đã được bán đấu giá thành công với giá {highest_bid.amount} JCoins."
                    )
                    # Gửi thông báo cho những người đã tham gia đấu giá nhưng không thắng cuộc
                    bidders = Bid.objects.filter(auction=self).exclude(user=highest_bid.user).values_list('user', flat=True).distinct()
                    for bidder_id in bidders:
                        Notification.objects.create(
                            user_id=bidder_id,
                            message=f"Phiên đấu giá cho trang sức '{auction_jewelry.name}' đã kết thúc. Rất tiếc bạn không phải là người chiến thắng."
                        )
                else:
                    # Xử lý trường hợp không tìm thấy FeeConfiguration
                    raise ValidationError("Fee configuration not found.")
            else:
                # Nếu không có bid nào, cập nhật trạng thái jewelry về 'NO_BIDS'
                auction_jewelry = self.jewelry
                auction_jewelry.status = 'NO_BIDS'
                auction_jewelry.save()

                # Tạo thông báo cho người bán
                Notification.objects.create(
                    user=auction_jewelry.owner,
                    message=f"Phiên đấu giá cho trang sức '{auction_jewelry.name}' của bạn đã kết thúc mà không có người đặt giá."
                )
        elif self.status != 'OPEN':
            raise ValidationError("Auction is not open.")
        else:
            raise ValidationError("Auction has not ended yet.")
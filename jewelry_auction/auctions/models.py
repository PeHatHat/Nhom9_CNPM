from django.db import models
from users.models import User
from jewelry.models import Jewelry
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import F, Max
from core.models import FeeConfiguration
from notifications.models import Notification
from django.db import transaction

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
        """Kiểm tra xem phiên đấu giá có đang mở hay không."""
        return self.status == 'OPEN'

    def open_auction(self):
        """Mở phiên đấu giá."""
        if self.status == 'CREATED' and self.start_time <= timezone.now():
            self.status = 'OPEN'
            self.save()

    def close_auction(self):
        """Đóng phiên đấu giá, cập nhật bid thắng, trạng thái jewelry, tạo giao dịch, trừ/cộng JCoin và gửi thông báo."""
        from bids.models import Bid
        from transactions.models import Transaction
        if self.status == 'OPEN' and self.end_time <= timezone.now():
            self.status = 'CLOSED'
            highest_bid = self.bids.select_related('user').order_by('-amount').first()

            with transaction.atomic():
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

                        transaction = Transaction.objects.create(
                            auction=self,
                            winning_bidder=highest_bid.user,
                            jewelry_owner=auction_jewelry.owner,
                            amount=transaction_amount,
                            fee=fee,
                            status='COMPLETED'
                        )

                        # Chuyển JCoin với F expressions và select_for_update()
                        User.objects.filter(pk=highest_bid.user.pk).select_for_update().update(jcoin_balance=F('jcoin_balance') - transaction_amount)
                        User.objects.filter(pk=auction_jewelry.owner.pk).select_for_update().update(jcoin_balance=F('jcoin_balance') + (transaction_amount - fee))

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
                        # Có thể log lỗi hoặc tạo thông báo cho admin
                        print("Fee configuration not found.")

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

                # Tạo thông báo cho manager và staff
                Notification.objects.create(
                    user=self.manager,
                    message=f"Phiên đấu giá cho trang sức '{self.jewelry.name}' đã kết thúc."
                )
                if self.staff:
                    Notification.objects.create(
                        user=self.staff,
                        message=f"Phiên đấu giá cho trang sức '{self.jewelry.name}' đã kết thúc."
                    )

        elif self.status != 'OPEN':
            raise ValidationError("Auction is not open.")
        else:
            raise ValidationError("Auction has not ended yet.")

    def save(self, *args, **kwargs):
        # Kiểm tra trạng thái của jewelry trước khi lưu
        if self.pk is None:  # Nếu là tạo mới
            if self.jewelry.status != 'APPROVED':
                raise ValidationError("Cannot create an auction for a jewelry that is not approved.")
        super().save(*args, **kwargs)

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be greater than start time.")
        if self.end_time <= timezone.now():
            raise ValidationError("End time must be in the future.")
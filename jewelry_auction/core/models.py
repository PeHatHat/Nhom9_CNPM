from django.db import models
from django.conf import settings

class JCoinManagement(models.Model):
    id = models.AutoField(primary_key=True)
    total_jcoin = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"Total JCoins: {self.total_jcoin}"

class FeeConfiguration(models.Model):
    id = models.AutoField(primary_key=True)
    fee_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.05)

    def __str__(self):
        return f"Fee Rate: {self.fee_rate}"

    def save(self, *args, **kwargs):
        if not self.pk and FeeConfiguration.objects.exists():
            # Chỉ cho phép một cấu hình phí
            raise Exception('There can be only one FeeConfiguration instance')
        super(FeeConfiguration, self).save(*args, **kwargs)

# Signal để cập nhật jcoin_balance của tất cả user
def update_user_jcoin_balance(sender, instance, **kwargs):
    if instance.jcoin_balance < 0:
        raise Exception("JCoin balance cannot be negative")

models.signals.pre_save.connect(update_user_jcoin_balance, sender=settings.AUTH_USER_MODEL)
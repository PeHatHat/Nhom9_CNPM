from django.db import models
from django.core.exceptions import ValidationError
from solo.models import SingletonModel

class FeeConfiguration(SingletonModel):
    id = models.AutoField(primary_key=True)
    fee_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.05)

    def __str__(self):
        return f"Fee Rate: {self.fee_rate}"

    def clean(self):
        if self.fee_rate < 0:
            raise ValidationError({'fee_rate': 'Fee rate cannot be negative.'})
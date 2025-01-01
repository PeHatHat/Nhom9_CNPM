from rest_framework import serializers
from .models import FeeConfiguration

class FeeConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeConfiguration
        fields = ['id', 'fee_rate']
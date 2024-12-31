from rest_framework import serializers
from .models import JCoinManagement, FeeConfiguration

class JCoinManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = JCoinManagement
        fields = '__all__'

class FeeConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeConfiguration
        fields = '__all__'
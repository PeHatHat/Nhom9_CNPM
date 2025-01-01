from rest_framework import serializers
from .models import Auction
from jewelry.models import Jewelry
from bids.serializers import BidSerializer
from django.utils import timezone
from django.core.exceptions import ValidationError

class AuctionSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True)
    start_time = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S'])
    end_time = serializers.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S'])
    
    class Meta:
        model = Auction
        fields = ['auction_id', 'jewelry', 'manager', 'staff', 'start_time', 'end_time', 'status', 'winning_bid', 'bids']
        read_only_fields = ['auction_id', 'status', 'winning_bid', 'bids', 'manager']

    def validate(self, data):
        if 'start_time' in data and 'end_time' in data:
            if data['start_time'] >= data['end_time']:
                raise serializers.ValidationError("End time must be greater than start time.")
            if data['end_time'] <= timezone.now():
                raise serializers.ValidationError("End time must be in the future.")
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['jewelry'] = instance.jewelry.jewelry_id
        return representation

    def create(self, validated_data):
        # Lấy thông tin người dùng từ request
        user = self.context['request'].user

        # Gán thông tin người dùng làm manager cho phiên đấu giá mới
        auction = Auction.objects.create(manager=user, **validated_data)

        return auction
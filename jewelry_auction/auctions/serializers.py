from rest_framework import serializers
from .models import Auction
from jewelry.models import Jewelry
from bids.serializers import BidSerializer
from django.utils import timezone

class AuctionSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True)
    jewelry_name = serializers.CharField(source='jewelry.name', read_only=True)
    jewelry_image = serializers.SerializerMethodField()
    highest_bid = serializers.SerializerMethodField()
    jewelry_owner = serializers.CharField(source='jewelry.owner', read_only=True)

    class Meta:
        model = Auction
        fields = ['auction_id', 'jewelry', 'jewelry_name', 'jewelry_image','jewelry_owner', 'manager', 'staff', 'start_time', 'end_time', 'status', 'winning_bid', 'bids', 'highest_bid']

    def get_jewelry_image(self, obj):
        if obj.jewelry.image_1:
            return obj.jewelry.image_1.url
        return None

    def get_highest_bid(self, obj):
        highest_bid = obj.bids.order_by('-amount').first()
        if highest_bid:
            return BidSerializer(highest_bid).data
        return None

class CreateAuctionFormSerializer(serializers.ModelSerializer):
    jewelry = serializers.PrimaryKeyRelatedField(queryset=Jewelry.objects.filter(is_approved=True))

    class Meta:
        model = Auction
        fields = ['start_time', 'end_time', 'jewelry']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("End time must be greater than start time.")
        if data['start_time'] < timezone.now():
            raise serializers.ValidationError("Start time must be greater than now.")
        return data

class AuctionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['start_time', 'end_time', 'status']  # Các trường Manager có thể cập nhật

    def validate(self, data):
        # Chỉ validate nếu 'start_time' và 'end_time' đều được cung cấp
        if 'start_time' in data and 'end_time' in data:
            if data['start_time'] >= data['end_time']:
                raise serializers.ValidationError("End time must be greater than start time.")
            if data['start_time'] < timezone.now():
                raise serializers.ValidationError("Start time must be greater than now.")

        return data
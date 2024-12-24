from rest_framework import serializers
from .models import Auction
from jewelry.models import Jewelry
from bids.serializers import BidSerializer

class AuctionSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True)
    class Meta:
        model = Auction
        fields = ['auction_id', 'jewelry', 'manager', 'staff', 'start_time', 'end_time', 'status', 'winning_bid', 'bids']

class CreateAuctionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jewelry'] = serializers.PrimaryKeyRelatedField(queryset=Jewelry.objects.filter(status='APPROVED'))
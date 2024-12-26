from rest_framework import serializers
from .models import Auction
from jewelry.models import Jewelry
from bids.serializers import BidSerializer

class AuctionSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True)
    jewelry_name = serializers.CharField(source='jewelry.name', read_only=True)
    jewelry_image = serializers.SerializerMethodField()
    jewelry_owner = serializers.CharField(source='jewelry.owner', read_only=True)

    class Meta:
        model = Auction
        fields = ['auction_id', 'jewelry', 'jewelry_name','jewelry_owner', 'jewelry_image', 'manager', 'staff', 'start_time', 'end_time', 'status', 'winning_bid', 'bids']

    def get_jewelry_image(self, obj):
        if obj.jewelry.image_1:
            return obj.jewelry.image_1.url
        return None

class CreateAuctionFormSerializer(serializers.ModelSerializer):
    jewelry = serializers.PrimaryKeyRelatedField(queryset=Jewelry.objects.filter(is_approved=True))

    class Meta:
        model = Auction
        fields = ['start_time', 'end_time', 'jewelry']
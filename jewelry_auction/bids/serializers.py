from rest_framework import serializers
from .models import Bid
from auctions.models import Auction
from django.core.exceptions import ValidationError

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['bid_id', 'auction', 'user', 'amount', 'timestamp']

class PlaceBidFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['amount']

    def validate(self, data):
        # Lấy auction_id thông qua request.parser_context
        auction_id = self.context['request'].parser_context['kwargs'].get('auction_id')
        auction = Auction.objects.get(pk=auction_id)
        
        # Kiểm tra nếu phiên đấu giá đã kết thúc
        if auction.status != 'OPEN':
            raise serializers.ValidationError("This auction is not open for bidding.")

        # Kiểm tra nếu người dùng không đủ JCoin
        if self.context['request'].user.jcoin_balance < data['amount']:
            raise serializers.ValidationError("You don't have enough JCoins to place this bid.")
        
        # Kiểm tra nếu user hiện tại đã đặt giá cao nhất
        highest_bid = Bid.objects.filter(auction=auction).order_by('-amount').first()
        if highest_bid and highest_bid.user == self.context['request'].user:
            raise serializers.ValidationError("You are already the highest bidder.")

        # Kiểm tra nếu giá thầu thấp hơn giá thầu cao nhất hiện tại
        if highest_bid:
            if data['amount'] <= highest_bid.amount:
                raise serializers.ValidationError('Your bid must be higher than the current highest bid.')
        else:
            if data['amount'] < auction.jewelry.initial_price:
                raise serializers.ValidationError(f'Your bid must be at least {auction.jewelry.initial_price}.')

        return data
from django.shortcuts import get_object_or_404
from .models import Bid
from auctions.models import Auction
from .serializers import PlaceBidFormSerializer, BidSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import AnonymousUser
from notifications.models import Notification

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_bid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)

    serializer = PlaceBidFormSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        with transaction.atomic():
            try:
                bid = serializer.save(user=request.user, auction=auction)
                
                # Lấy danh sách tất cả các bids cho phiên đấu giá này, trừ bid vừa được tạo
                other_bids = Bid.objects.filter(auction=auction).exclude(bid_id=bid.bid_id)

                # Tạo thông báo cho những người dùng đã đặt giá thầu trước đó
                for other_bid in other_bids:
                    Notification.objects.create(
                        user=other_bid.user,
                        message=f"Giá thầu của bạn cho trang sức '{auction.jewelry.name}' đã bị vượt qua. Giá thầu mới nhất là {bid.amount} JCoins."
                    )
                
                # Tạo thông báo cho người dùng đã đặt giá thầu thành công
                Notification.objects.create(
                    user=request.user,
                    message=f"Bạn đã đặt giá thầu thành công cho trang sức '{auction.jewelry.name}' với giá {bid.amount} JCoins."
                )

                return Response({"message": "Your bid has been placed successfully.", "bid_amount": bid.amount}, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserBidsList(generics.ListAPIView):
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, AnonymousUser):
            return Bid.objects.none()
        else:
            queryset = Bid.objects.filter(user=user).order_by('-timestamp')
            return queryset
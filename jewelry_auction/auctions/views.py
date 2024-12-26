from django.shortcuts import get_object_or_404
from .models import Auction
from jewelry.models import Jewelry
from bids.models import Bid
from transactions.models import Transaction
from .serializers import AuctionSerializer, CreateAuctionFormSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django.utils import timezone
from core.models import FeeConfiguration
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q

class AuctionList(generics.ListAPIView):
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated] # Chỉ cho phép user đã đăng nhập
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['start_time', 'end_time', 'status']
    search_fields = ['jewelry__name']

    def get_queryset(self):
        queryset = Auction.objects.all()

        # Filter by status
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        # Filter by user's auctions (optional)
        show_my_auctions = self.request.query_params.get('my_auctions', 'false').lower() == 'true'
        if show_my_auctions:
            user = self.request.user
            queryset = queryset.filter(Q(bids__user=user) | Q(jewelry__owner=user)).distinct()

        # Không gọi close_auction() ở đây nữa

        return queryset

class AuctionDetail(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Lấy đối tượng Auction dựa trên URL
        auction = super().get_object()

        # Chỉ gọi close_auction() khi cần thiết (ví dụ: khi xem chi tiết)
        auction.close_auction()

        return auction

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_auction(request, jewelry_id):
    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    # Check if the user is authorized to create an auction
    if request.user.role != 'MANAGER' and request.user.role != 'STAFF':
        return Response({"detail": "You are not authorized to create an auction."}, status=status.HTTP_403_FORBIDDEN)

    # Check if the jewelry is approved
    if not jewelry.is_approved: # Thay đổi kiểm tra is_approved
        return Response({"detail": "This jewelry is not approved for auction."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CreateAuctionFormSerializer(data=request.data)
    if serializer.is_valid():
        auction = serializer.save(manager=request.user, status='CREATED') # Bỏ jewelry=jewelry
        return Response(AuctionSerializer(auction).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
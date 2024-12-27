from django.shortcuts import get_object_or_404
from .models import Auction
from jewelry.models import Jewelry
from bids.models import Bid
from transactions.models import Transaction
from .serializers import AuctionSerializer, CreateAuctionFormSerializer, AuctionUpdateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django.utils import timezone
from core.models import FeeConfiguration
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q
from rest_framework.decorators import action

class AuctionList(generics.ListAPIView):
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['start_time', 'end_time', 'status']
    search_fields = ['jewelry__name']

    def get_queryset(self):
        queryset = Auction.objects.filter(status__in=['OPEN', 'CLOSED'])

        # Filter by status
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        # Filter by user's auctions (optional)
        show_my_auctions = self.request.query_params.get('my_auctions', 'false').lower() == 'true'
        if show_my_auctions:
            user = self.request.user
            queryset = queryset.filter(Q(bids__user=user) | Q(jewelry__owner=user)).distinct()

        return queryset

class AuctionDetail(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Lấy đối tượng Auction dựa trên URL
        auction = super().get_object()
        return auction

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_auction(request, jewelry_id):
    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    # Check if the user is authorized to create an auction
    if request.user.role != 'MANAGER' and request.user.role != 'STAFF':
        return Response({"detail": "You are not authorized to create an auction."}, status=status.HTTP_403_FORBIDDEN)

    # Check if the jewelry is approved
    if not jewelry.is_approved:
        return Response({"detail": "This jewelry is not approved for auction."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CreateAuctionFormSerializer(data=request.data)
    if serializer.is_valid():
        auction = serializer.save(manager=request.user, status='CREATED')
        return Response(AuctionSerializer(auction).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuctionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Lấy đối tượng Auction dựa trên URL
        auction = super().get_object()
        return auction

    def put(self, request, *args, **kwargs):
        # Chỉ cho phép Manager, Staff, Admin cập nhật phiên đấu giá
        if request.user.role not in ['MANAGER', 'STAFF', 'ADMIN']:
            return Response({"detail": "You are not authorized to update an auction."}, status=status.HTTP_403_FORBIDDEN)

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Chỉ cho phép Manager, Staff, Admin cập nhật phiên đấu giá
        if request.user.role not in ['MANAGER', 'STAFF', 'ADMIN']:
            return Response({"detail": "You are not authorized to update an auction."}, status=status.HTTP_403_FORBIDDEN)

        return self.partial_update(request, *args, **kwargs)
    
    def get_serializer_class(self):
        # Sử dụng AuctionUpdateSerializer cho các request PUT (cập nhật)
        if self.request.method == 'PUT':
            return AuctionUpdateSerializer
        return AuctionSerializer

    @action(detail=True, methods=['PATCH'])
    def cancel(self, request, pk=None):
        auction = self.get_object()

        if request.user.role not in ['MANAGER', 'ADMIN']:
            return Response({"detail": "You are not authorized to cancel this auction."}, status=status.HTTP_403_FORBIDDEN)
        
        if auction.status == 'CANCELED':
            return Response({"detail": "Auction is already canceled."}, status=status.HTTP_400_BAD_REQUEST)

        if auction.status == 'CLOSED':
            return Response({"detail": "Auction is already closed."}, status=status.HTTP_400_BAD_REQUEST)

        if auction.status == 'CREATED':
            auction.status = 'CANCELED'
            auction.save()
            return Response({"message": "Auction canceled successfully."})

        auction.status = 'CANCELED'
        auction.save()

        return Response({"message": "Auction canceled successfully."})
from django.shortcuts import get_object_or_404
from .models import Auction
from jewelry.models import Jewelry
from bids.models import Bid
from transactions.models import Transaction
from .serializers import AuctionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from core.models import FeeConfiguration
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import transaction

class AuctionList(generics.ListAPIView):
    serializer_class = AuctionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Auction.objects.all()
        # Lọc các phiên đấu giá dựa trên trạng thái
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset

class AuctionDetail(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_auction(request, jewelry_id):
    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    # Check if the user is authorized to create an auction
    if request.user.role not in ['MANAGER', 'STAFF']:
        return Response({"detail": "You are not authorized to create an auction."}, status=status.HTTP_403_FORBIDDEN)

    # Check if the jewelry is approved
    if jewelry.status != 'APPROVED':
        return Response({"detail": "This jewelry is not approved for auction."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = AuctionSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            auction = serializer.save(jewelry=jewelry, manager=request.user, status='CREATED')
            jewelry.status = 'AUCTIONING'
            jewelry.save()
        return Response(AuctionSerializer(auction).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
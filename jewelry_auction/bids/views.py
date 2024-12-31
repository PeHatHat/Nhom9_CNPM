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

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_bid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)

    serializer = PlaceBidFormSerializer(data=request.data, context={'request': request}) # Sửa lại dòng này
    if serializer.is_valid():
        with transaction.atomic():
            try:
                bid = serializer.save(user=request.user, auction=auction)
                return Response({"message": "Your bid has been placed successfully.", "bid_amount": bid.amount}, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserBidsList(generics.ListAPIView):
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(f"DEBUG: User: {user}")
        if isinstance(user, AnonymousUser):
            print("DEBUG: User is AnonymousUser")
            return Bid.objects.none()
        else:
            print(f"DEBUG: User ID: {user.user_id}")
            print(f"DEBUG: Username: {user.username}")
            queryset = Bid.objects.filter(user=user).order_by('-timestamp')
            print(f"DEBUG: Queryset: {queryset}")
            print(f"DEBUG: Queryset Count: {queryset.count()}")
            return queryset
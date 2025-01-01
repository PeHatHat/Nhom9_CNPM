from django.shortcuts import get_object_or_404
from .models import Auction
from jewelry.models import Jewelry
from .serializers import AuctionSerializer
from rest_framework.decorators import api_view, permission_classes , action
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from django.utils import timezone
from core.models import FeeConfiguration
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import transaction
from core.permissions import IsManager
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from notifications.models import Notification

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

    def get_permissions(self):
        """
        Phân quyền cho các action của Auction.
        """
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsManager]
        elif self.action in ['update', 'partial_update', 'destroy', 'cancel_auction']:
            permission_classes = [IsAuthenticated, IsManager]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]  # Cho phép tất cả user xem danh sách và chi tiết
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Lọc queryset dựa trên trạng thái nếu user là Manager.
        """
        user = self.request.user
        queryset = Auction.objects.all()  # Bắt đầu với tất cả auctions

        if user.is_authenticated:
            if user.role == 'MANAGER':
                status = self.request.query_params.get('status')
                if status:
                    queryset = queryset.filter(status=status)
            else:
                # Cho phép các user đã đăng nhập khác xem các auction có trạng thái OPEN hoặc CLOSED
                queryset = queryset.filter(status__in=['OPEN', 'CLOSED'])

        return queryset

    def perform_create(self, serializer):
        # Lấy thông tin jewelry_id từ validated_data
        jewelry_id = serializer.validated_data.get('jewelry').jewelry_id
        if not jewelry_id:
            raise ValidationError("Jewelry ID is required in the request body.")

        # Lấy đối tượng Jewelry từ database
        jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

        # Kiểm tra xem jewelry đã được approved chưa
        if jewelry.status != 'APPROVED':
            raise ValidationError("Jewelry must be approved before creating an auction.")
        
        # Kiểm tra role của người dùng
        if self.request.user.role != 'MANAGER':
            raise ValidationError("Only managers can create auctions.")

        # Gán jewelry và manager vào serializer và lưu
        auction = serializer.save(jewelry=jewelry, manager=self.request.user)

        # Tạo thông báo cho người bán khi phiên đấu giá được tạo
        Notification.objects.create(
            user=jewelry.owner,
            message=f"Phiên đấu giá cho trang sức '{jewelry.name}' của bạn đã được tạo và sẽ bắt đầu vào lúc {auction.start_time}."
        )

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsManager])
    @csrf_exempt
    def cancel_auction(self, request, pk=None):
        auction = self.get_object()
        if auction.status == 'CREATED':
            auction.status = 'CANCELED'
            auction.save()

            # Tạo thông báo cho người bán khi phiên đấu giá bị hủy
            Notification.objects.create(
                user=auction.jewelry.owner,
                message=f"Phiên đấu giá cho trang sức '{auction.jewelry.name}' của bạn đã bị hủy."
            )

            serializer = self.get_serializer(auction)
            return Response(serializer.data)
        else:
            return Response({"detail": "Auction can only be canceled if it is in 'CREATED' status."}, status=status.HTTP_400_BAD_REQUEST)
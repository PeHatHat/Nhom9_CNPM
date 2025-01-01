from rest_framework import viewsets, filters, status
from .models import Jewelry
from .serializers import JewelrySerializer, JewelryCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from notifications.models import Notification

# Tạo class check quyền cho từng action
class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kiểm tra xem user có phải là owner của object hay không
        return obj.owner == request.user or request.user.role in ['STAFF', 'MANAGER']

# Tạo class check quyền Staff
class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['STAFF', 'MANAGER']

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'MEMBER'

class JewelryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class JewelryViewSet(viewsets.ModelViewSet):
    serializer_class = JewelrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['initial_price', 'name']
    pagination_class = JewelryPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.role in ['STAFF', 'MANAGER']:
                if self.request.query_params.get('is_approved') == 'false':
                    queryset = Jewelry.objects.filter(status='PENDING')
                else:
                    queryset = Jewelry.objects.all()
            else:
                queryset = Jewelry.objects.filter(status__in=['APPROVED', 'AUCTIONING', 'NO_BIDS'])
        else:
            # Nếu người dùng chưa đăng nhập, chỉ hiển thị các trang sức đã được duyệt, đang đấu giá hoặc chưa có bid
            queryset = Jewelry.objects.filter(status__in=['APPROVED', 'AUCTIONING', 'NO_BIDS'])
        # Các phần lọc khác
        ordering = self.request.query_params.get('sort')
        if ordering:
            if ordering.startswith('-'):
                queryset = queryset.order_by(ordering)
            else:
                queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('-jewelry_id') # Thêm dòng này để có thứ tự mặc định
            
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))

        return queryset

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMember]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        elif self.action == 'my_jewelry':
            permission_classes = [IsAuthenticated, IsMember]
        elif self.action in ['approve_jewelry', 'reject_jewelry', 'update_jewelry']:
            permission_classes = [IsAuthenticated, IsStaff]
        elif self.action == 'confirm_auction':
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return JewelryCreateSerializer
        return JewelrySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, IsMember])
    def my_jewelry(self, request):
        user = request.user
        user_jewelry = Jewelry.objects.filter(owner=user)
        serializer = self.get_serializer(user_jewelry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsStaff])
    @csrf_exempt
    def update_jewelry(self, request, pk=None):
        jewelry = self.get_object()

        # Cho phép staff cập nhật các trường preliminary_price, final_price, received_at
        if 'preliminary_price' in request.data:
            jewelry.preliminary_price = request.data['preliminary_price']
        if 'final_price' in request.data:
            jewelry.final_price = request.data['final_price']
        if 'received_at' in request.data:
            jewelry.received_at = request.data['received_at']

        jewelry.save()
        serializer = self.get_serializer(jewelry)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsOwnerOrStaff])
    @csrf_exempt
    def confirm_auction(self, request, pk=None):
        jewelry = self.get_object()

        # Kiểm tra xem trạng thái của trang sức có phải là 'APPROVED' không
        if jewelry.status != 'APPROVED':
            return Response({"detail": "Jewelry is not approved for auction confirmation."}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra xem người dùng có phải là chủ sở hữu của trang sức không
        if request.user != jewelry.owner:
            return Response({"detail": "You are not the owner of this jewelry."}, status=status.HTTP_403_FORBIDDEN)

        # Cho phép owner cập nhật seller_approved
        if 'seller_approved' in request.data:
            jewelry.seller_approved = request.data['seller_approved']
        jewelry.save()
        serializer = self.get_serializer(jewelry)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsStaff])
    @csrf_exempt
    def approve_jewelry(self, request, pk=None):
        jewelry = self.get_object()
        jewelry.status = 'APPROVED'
        jewelry.save()

        # Tạo thông báo cho người dùng
        Notification.objects.create(
            user=jewelry.owner,
            message=f"Trang sức '{jewelry.name}' của bạn đã được duyệt và sẽ sớm được đưa vào danh sách đấu giá."
        )

        serializer = self.get_serializer(jewelry)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsStaff])
    @csrf_exempt
    def reject_jewelry(self, request, pk=None):
        jewelry = self.get_object()
        jewelry.status = 'REJECTED'
        jewelry.save()

        # Tạo thông báo cho người dùng
        Notification.objects.create(
            user=jewelry.owner,
            message=f"Trang sức '{jewelry.name}' của bạn đã bị từ chối."
        )

        serializer = self.get_serializer(jewelry)
        return Response(serializer.data)
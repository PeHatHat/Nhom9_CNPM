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

# Tạo class check quyền cho từng action
class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kiểm tra xem user có phải là owner của object hay không
        return obj.owner == request.user or request.user.role in ['STAFF', 'MANAGER']
        
class JewelryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class JewelryViewSet(viewsets.ModelViewSet):  # Kế thừa từ ModelViewSet
    serializer_class = JewelrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['initial_price', 'name']
    pagination_class = JewelryPagination

    def get_queryset(self):
        # print("DEBUG: JewelryViewSet get_queryset called")
        queryset = Jewelry.objects.filter(status__in=['APPROVED', 'AUCTIONING', 'NO_BIDS'])

        ordering = self.request.query_params.get('sort')
        if ordering:
            if ordering.startswith('-'):
                queryset = queryset.order_by(ordering)
            else:
                queryset = queryset.order_by(ordering)

        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))

        return queryset

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return JewelryCreateSerializer
        return JewelrySerializer

    def list(self, request, *args, **kwargs):
        # print("DEBUG: JewelryViewSet list called")
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # print(f"DEBUG: Serialized Data: {serializer.data}")
        return Response(serializer.data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_jewelry(self, request):
        # print("DEBUG: JewelryViewSet my_jewelry called")
        user = request.user
        # print(f"DEBUG: User: {user}")
        # print(f"DEBUG: User ID: {user.user_id}")
        # print(f"DEBUG: User PK: {user.pk}")
        # print(f"DEBUG: Username: {user.username}")
        user_jewelry = Jewelry.objects.filter(owner=user)
        # print(f"DEBUG: User Jewelry Queryset: {user_jewelry}")
        # print(f"DEBUG: User Jewelry Count: {user_jewelry.count()}")
        serializer = self.get_serializer(user_jewelry, many=True)
        # print(f"DEBUG: Serialized Data: {serializer.data}")
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
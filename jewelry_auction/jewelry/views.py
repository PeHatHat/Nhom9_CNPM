from rest_framework import viewsets, filters, status, generics
from .models import Jewelry
from .serializers import JewelrySerializer, JewelryCreateSerializer, MyJewelrySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from django.shortcuts import get_object_or_404
from .permissions import IsStaffUser, IsManagerUser

class JewelryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class JewelryFilter(django_filters.FilterSet):
    class Meta:
        model = Jewelry
        fields = {
            'name': ['icontains'],
            'status': ['exact'],
            'is_approved': ['exact'],
        }

class JewelryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JewelrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = JewelryFilter
    ordering_fields = ['initial_price', 'name']
    search_fields = ['name']
    pagination_class = JewelryPagination

    def get_queryset(self):
        queryset = Jewelry.objects.all()
        return queryset

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_jewelry(request):
    if request.user.role not in ['MEMBER', 'ADMIN']:
        return Response({"detail": "You are not authorized to create jewelry."}, status=status.HTTP_403_FORBIDDEN)

    serializer = JewelryCreateSerializer(data=request.data)
    if serializer.is_valid():
        jewelry = serializer.save(owner=request.user, status='PENDING')
        return Response(JewelrySerializer(jewelry).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffJewelryViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser | IsStaffUser | IsManagerUser]

    @action(detail=True, methods=['POST'])
    def approve(self, request, pk=None):
        jewelry = get_object_or_404(Jewelry, pk=pk)
        if request.user.role not in ['STAFF', 'MANAGER', 'ADMIN']:
            return Response({"detail": "You are not authorized to approve jewelry."}, status=status.HTTP_403_FORBIDDEN)

        if jewelry.status != 'PENDING':
            return Response({"detail": "This jewelry is not pending approval."}, status=status.HTTP_400_BAD_REQUEST)

        jewelry.is_approved = True
        jewelry.status = 'APPROVED'
        jewelry.is_read = False  # Member chưa đọc thông báo
        jewelry.save()

        return Response({"message": "Jewelry approved"})

    @action(detail=True, methods=['POST'])
    def reject(self, request, pk=None):
        # ... (tương tự như approve, nhưng set is_approved = False, status = 'REJECTED', is_read = False)
        jewelry = get_object_or_404(Jewelry, pk=pk)
        
        # Check if the user is authorized
        if request.user.role not in ['STAFF', 'MANAGER', 'ADMIN']:
            return Response({"detail": "You are not authorized to approve jewelry."}, status=status.HTTP_403_FORBIDDEN)

        if jewelry.status != 'PENDING':
            return Response({"detail": "This jewelry is not pending approval."}, status=status.HTTP_400_BAD_REQUEST)

        jewelry.is_approved = False
        jewelry.status = 'REJECTED'
        jewelry.is_read = False
        jewelry.save()

        return Response({"message": "Jewelry rejected"})

class MyJewelryList(generics.ListAPIView):
    serializer_class = MyJewelrySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = JewelryPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Jewelry.objects.filter(owner=user)

        # Đánh dấu tất cả thông báo là đã đọc khi user xem danh sách
        queryset.filter(is_read=False).update(is_read=True)

        return queryset
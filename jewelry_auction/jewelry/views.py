from rest_framework import viewsets, filters
from .models import Jewelry
from .serializers import JewelrySerializer
from rest_framework.permissions import AllowAny
from django.db.models import Q

class JewelryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Jewelry.objects.filter(is_approved=True)
    serializer_class = JewelrySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['initial_price']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))
        return queryset
from rest_framework import viewsets, filters, status
from .models import Jewelry
from .serializers import JewelrySerializer
from rest_framework.permissions import AllowAny
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class JewelryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class JewelryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JewelrySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['initial_price', 'name']
    pagination_class = JewelryPagination

    def get_queryset(self):
        queryset = Jewelry.objects.filter(is_approved=True)
        print("Before filtering:", str(queryset.query))

        ordering = self.request.query_params.get('sort')
        if ordering:
            if ordering.startswith('-'):
                queryset = queryset.order_by(ordering)
            else:
                queryset = queryset.order_by(ordering)
            print("After ordering:", str(queryset.query))

        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))
            print("After searching:", str(queryset.query))

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
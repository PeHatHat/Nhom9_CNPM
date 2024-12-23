from rest_framework import viewsets, filters
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import AllowAny
from django.db.models import Q

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['publication_date', 'title']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Apply ordering
        ordering = self.request.query_params.get('sort')
        if ordering:
            if ordering.startswith('-'):
                queryset = queryset.order_by(ordering)
            else:
                queryset = queryset.order_by(ordering)
            print("After ordering:", str(queryset.query))

        # Apply search filter
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))
            print("After searching:", str(queryset.query))

        return queryset
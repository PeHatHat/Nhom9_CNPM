from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FeeConfiguration
from .serializers import FeeConfigurationSerializer
from rest_framework.decorators import action
from rest_framework import status
from core.permissions import IsAdmin
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import User

def home(request):
    # Lấy danh sách bài viết từ API
    blog_response = requests.get(f'{settings.BASE_URL}/api/blogs/')
    blog_posts = blog_response.json() if blog_response.status_code == 200 else []

    # Lấy danh sách trang sức từ API
    jewelry_response = requests.get(f'{settings.BASE_URL}/api/jewelry/')
    jewelry_products = jewelry_response.json() if jewelry_response.status_code == 200 else []

    # Truyền dữ liệu vào context
    context = {
        'blog_posts': blog_posts,
        'jewelry_products': jewelry_products,
    }
    return render(request, 'core/index.html', context)

class FeeConfigurationViewSet(viewsets.ModelViewSet):
    queryset = FeeConfiguration.objects.all()
    serializer_class = FeeConfigurationSerializer
    permission_classes = [IsAdmin]

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['PUT'], permission_classes=[IsAdmin])
    @csrf_exempt
    def manage_jcoin(self, request, user_id=None):
        if not user_id:
            return Response({"error": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        amount = request.data.get('amount')
        if amount is None:
            return Response({"error": "Amount is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = int(amount)
        except ValueError:
            return Response({"error": "Amount must be an integer."}, status=status.HTTP_400_BAD_REQUEST)

        user.jcoin_balance += amount
        user.save()

        return Response({"message": f"JCoin balance updated for user {user.username}. New balance: {user.jcoin_balance}"}, status=status.HTTP_200_OK)
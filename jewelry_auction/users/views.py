from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.db import transaction
from core.permissions import IsAdmin
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    with transaction.atomic():
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)  # Tạo hoặc lấy token
            return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['put'], permission_classes=[IsAdmin])
    def manage_jcoin(self, request, pk=None):
        user = self.get_object()
        amount = request.data.get('amount')

        if not isinstance(amount, int) and not isinstance(amount, float):
            return Response({"error": "Amount must be a number."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user.jcoin_balance += amount
            user.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_notifications(self, request):
        notifications = Notification.objects.filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
from django.http import HttpResponse
from django.core.management import call_command
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.conf import settings
import os
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import JCoinManagement, FeeConfiguration
from users.models import User
from .serializers import JCoinManagementSerializer, FeeConfigurationSerializer  # Xóa UserSerializer ở đây
from users.serializers import UserSerializer  # Import UserSerializer từ users.serializers
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from jewelry.models import Jewelry
from auctions.models import Auction

from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html') # Sửa 'core/index.html' nếu bạn dùng template khác

@api_view(['GET', 'PUT'])
@permission_classes([IsAdminUser])
def manage_jcoin(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            # Kiểm tra logic nghiệp vụ (ví dụ: jcoin_balance không âm)
            if serializer.validated_data.get('jcoin_balance') is not None and serializer.validated_data['jcoin_balance'] < 0:
                return Response({"detail": "JCoin balance cannot be negative."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([IsAdminUser])
def manage_fee(request):
    fee_config = FeeConfiguration.objects.first()  # Chỉ lấy một cấu hình

    if request.method == 'GET':
        serializer = FeeConfigurationSerializer(fee_config)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeeConfigurationSerializer(fee_config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def backup_db(request):
    try:
        # Tạo thư mục media/db_backup nếu chưa tồn tại
        backup_dir = os.path.join(settings.MEDIA_ROOT, 'db_backup')
        os.makedirs(backup_dir, exist_ok=True)

        # Tạo tên file backup với timestamp
        timestamp = timezone.now().strftime("%Y%m%d-%H%M%S")
        file_name = f"db_backup_{timestamp}.json"
        file_path = os.path.join(backup_dir, file_name)

        # Thực hiện dumpdata và lưu vào file
        with open(file_path, 'w') as f:
            call_command('dumpdata', '--indent=4', stdout=f)

        # Trả về file cho người dùng download
        with open(file_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def restore_db(request):
    # Cần validate và xử lý file upload cẩn thận ở đây
    file = request.FILES.get('file')
    if not file:
        return Response({"detail": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Lưu file upload vào thư mục tạm
        temp_dir = os.path.join(settings.MEDIA_ROOT, 'db_backup', 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Thực hiện loaddata
        call_command('loaddata', file_path)

        # Xóa file tạm
        os.remove(file_path)

        return Response({"message": "Database restored successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
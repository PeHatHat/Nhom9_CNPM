from rest_framework import serializers
from .models import Jewelry
from users.models import User
from django.core.exceptions import ValidationError

class JewelrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = ['jewelry_id', 'name', 'description', 'owner', 'initial_price', 'image_1', 'image_2', 'image_3', 'status', 'preliminary_price', 'final_price', 'received_at', 'seller_approved']
        read_only_fields = ['owner']

class JewelryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = ['name', 'description', 'initial_price', 'image_1', 'image_2', 'image_3']

    def create(self, validated_data):
        # Lấy user hiện tại từ request
        user = self.context['request'].user

        # Kiểm tra nếu user là AnonymousUser
        if user.is_anonymous:
            raise serializers.ValidationError("User must be logged in to create a jewelry.")

        # Kiểm tra nếu user không có quyền MEMBER
        if user.role != 'MEMBER':
            raise serializers.ValidationError("User does not have permission to create a jewelry.")

        # Tạo Jewelry object với owner là user hiện tại
        jewelry = Jewelry.objects.create(owner=user, **validated_data)
        return jewelry

    def validate_initial_price(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Initial price must be greater than zero.")
        return value
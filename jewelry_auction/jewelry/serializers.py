from rest_framework import serializers
from .models import Jewelry

class JewelrySerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Jewelry
        fields = ['jewelry_id', 'name', 'description', 'owner', 'owner_username', 'initial_price', 'image_1', 'image_2', 'image_3', 'status', 'is_approved']

class JewelryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = ['name', 'description', 'initial_price', 'image_1', 'image_2', 'image_3']

    def validate_image_1(self, value):
        if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            raise serializers.ValidationError("Invalid file format. Only PNG, JPG, JPEG, and GIF are allowed.")

        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Image file too large ( > 5MB )")

        return value

class MyJewelrySerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Jewelry
        fields = ['jewelry_id', 'name', 'description', 'initial_price', 'status', 'status_display', 'is_approved', 'is_read']
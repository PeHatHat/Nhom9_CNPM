from rest_framework import serializers
from .models import Jewelry

class JewelrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = ['jewelry_id', 'name', 'description', 'owner', 'initial_price', 'image_1', 'image_2', 'image_3', 'status', 'is_approved']
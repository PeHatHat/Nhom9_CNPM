from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'role', 'jcoin_balance']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    jcoin_balance = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, default=0)
    role = serializers.CharField(required=False, default='MEMBER')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'password_confirm', 'jcoin_balance', 'role']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'role', 'jcoin_balance', 'is_active', 'is_staff', 'is_superuser']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'role', 'jcoin_balance', 'is_active', 'is_staff'] # Các trường Admin có thể cập nhật
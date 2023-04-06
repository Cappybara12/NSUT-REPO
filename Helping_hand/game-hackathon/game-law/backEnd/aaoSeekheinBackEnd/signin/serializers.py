from rest_framework.serializers import ModelSerializer
from .models import AsUser


class UserViewSerializer(ModelSerializer):
    class Meta:
        model = AsUser
        fields = ['id', 'name', 'phone', 'createdAt','otp']
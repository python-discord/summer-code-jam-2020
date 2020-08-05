from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from retro_news.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for new user creation."""

    email = serializers.CharField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Hash password before saving it to DB."""
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

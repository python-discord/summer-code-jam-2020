from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from retro_news.models import CustomUser, BlogArticle


class BlogArticleSerializer(serializers.ModelSerializer):
    """Serializer for BlogArticle objects."""
    class Meta:
        model   = BlogArticle
        fields  = ('title','author','content','date_created')

class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for new user creation."""

    email = serializers.EmailField(required=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token obtain serializer to include superuser status to response."""

    def validate(self, attrs):
        """Add superuser field to response."""
        data = super().validate(attrs)
        data['superuser'] = self.user.is_superuser
        return data

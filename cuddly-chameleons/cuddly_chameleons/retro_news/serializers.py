from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from retro_news.models import ArticleComment, CustomUser, BlogArticle


class BlogArticleSerializer(serializers.ModelSerializer):
    """Serializer for BlogArticle objects."""

    title = serializers.CharField(max_length=100, required=True)
    content = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = BlogArticle
        fields = ('title', 'author', 'content')


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


class CustomUserSuperuserSerializer(serializers.ModelSerializer):
    """Serializer that contains basic user information for fetching."""

    is_superuser = serializers.BooleanField()

    class Meta:
        model = CustomUser
        fields = ('is_superuser',)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token obtain serializer to include superuser status to response."""

    def validate(self, attrs):
        """Add superuser field to response."""
        data = super().validate(attrs)
        data['superuser'] = self.user.is_superuser
        return data


class BlogArticleGetSerializer(serializers.ModelSerializer):
    """Serializer for BlogArticle objects getting."""

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, required=True)
    content = serializers.CharField()
    author = CustomUserSerializer(read_only=True, many=False)
    created = serializers.DateTimeField()

    class Meta:
        model = BlogArticle
        fields = ('id', 'title', 'content', 'author', 'created')


class ArticleCommentSerializer(serializers.ModelSerializer):
    """Serializer for ArticleComment model."""

    comment = serializers.CharField(max_length=10000)
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    post = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = ArticleComment
        fields = ('comment', 'author', 'post')


class GetArticleCommentSerializer(serializers.ModelSerializer):
    """Serializer for ArticleComment getting."""

    id = serializers.IntegerField(read_only=True)
    comment = serializers.CharField(max_length=10000)
    author = CustomUserSerializer(read_only=True, many=False)
    post = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    created = serializers.DateTimeField()

    class Meta:
        model = ArticleComment
        fields = ('id', 'comment', 'author', 'post', 'created')

from django.http import Http404
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from retro_news import serializers
from retro_news.models import BlogArticle, ArticleComment


class BlogArticleListView(APIView):
    """Handles BlogArticle object listing and creation."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request: Request):
        """Get all articles."""
        if "title" in request.query_params:
            return Response(
                serializers.BlogArticleGetSerializer(
                    BlogArticle.objects.filter(title__icontains=request.query_params["title"]),
                    many=True
                ).data
            )

        return Response(
            serializers.BlogArticleGetSerializer(
                BlogArticle.objects.all().order_by('-id'),
                many=True
            ).data
        )

    def post(self, request: Request):
        """Create new article."""
        if not request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = serializers.BlogArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save(author=request.user)
            if article:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogArticleActionView(APIView):
    """Handles specific article actions."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk: int):
        """Get object based on primary key."""
        try:
            return BlogArticle.objects.get(pk=pk)
        except BlogArticle.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int):
        """Get one blog post by primary key."""
        post = self.get_object(pk)
        return Response(serializers.BlogArticleGetSerializer(post).data)

    def put(self, request: Request, pk: int):
        """Update blog post by primary key."""
        if not request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        post = self.get_object(pk)
        serializer = serializers.BlogArticleSerializer(post, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        """Delete blog post by primary key."""
        if not request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomUserCreate(APIView):
    """Handles user creation."""

    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request: Request):
        """Create new user."""
        serializer = serializers.CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(APIView):
    """Handles JWT Token deactivating."""

    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request: Request):
        """Deactivate user JWT token."""
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    """Define custom token pair view to include superuser status inside response."""
    serializer_class = serializers.CustomTokenObtainPairSerializer


class IsSuperUserView(APIView):
    """View to get superuser information about user."""

    permissions_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request):
        """Get user's superuser status."""
        return Response(serializers.CustomUserSuperuserSerializer(request.user).data)


class ArticleCommentListView(APIView):
    """View for fetching all articles and creating new comment."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request: Request):
        """Get all comments. Add `post` query parameter to filter all comments that is connected with this post."""
        if "post" in request.query_params:
            return Response(
                serializers.GetArticleCommentSerializer(
                    ArticleComment.objects.get(
                        post=int(request.query_params['post'])
                    ),
                    many=True
                ).data
            )

        return Response(
            serializers.GetArticleCommentSerializer(
                ArticleComment.objects.all(),
                many=True
            ).data
        )

    def post(self, request: Request):
        """Create a new article comment."""
        serializer = serializers.ArticleCommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(author=request.user, post=BlogArticle.objects.get(pk=int(request.data['post'])))
            if comment:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

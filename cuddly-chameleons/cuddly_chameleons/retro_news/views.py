from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from retro_news.serializers import CustomUserSerializer


class CustomUserCreate(APIView):
    """Handles user creation."""

    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request: Request):
        """Create new user."""
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(APIView):
    """Handles JWT Token deactivating."""

    def post(self, request: Request):
        """Deactivate user JWT token."""
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

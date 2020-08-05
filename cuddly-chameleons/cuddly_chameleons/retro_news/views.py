from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from retro_news.serializers import CustomUserSerializer


class CustomUserCreate(APIView):
    """Handles user creation."""

    permission_classes = (permissions.AllowAny,)

    def post(self, request: Request, format=None):
        """Create new user."""
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

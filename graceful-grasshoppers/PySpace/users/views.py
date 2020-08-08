from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        """Optionally restricts the returned users to a given user
        by filtering against a `username` query parameter in the URL"""
        queryset = models.CustomUser.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


class LoggedInUserView(APIView):
    """Returns information about currently logged in user"""
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        print(user)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

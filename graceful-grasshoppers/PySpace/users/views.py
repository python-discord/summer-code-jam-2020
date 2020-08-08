from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from random import choice

# Create your views here.


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        """Optionally restricts the returned users to a given user
        by filtering against a `username` query parameter in the URL"""
        queryset = models.CustomUser.objects.all()
        username = self.request.query_params.get('username', None)
        random_param = self.request.query_params.get('random', None)
        if random_param is not None:
            print(queryset)
            random_user_id = choice([user.id for user in queryset])
            queryset = models.CustomUser.objects.filter(id=random_user_id)
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

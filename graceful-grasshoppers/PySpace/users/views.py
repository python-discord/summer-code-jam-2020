# from django.shortcuts import render
from rest_framework import generics
import api.models as api_models
from . import models
from . import serializers

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

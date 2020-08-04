from django.shortcuts import render
from rest_framework import viewsets
from fbbackend import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

'''
Views for our Rest API.
We went with class based views, because they were a better fit than functions
'''

class Account_View(viewsets.ModelViewSet): #Allow you to view all Accounts and Create New ones
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

class Group_View(viewsets.ModelViewSet): #Allow you to view all Groups and Create New ones
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer









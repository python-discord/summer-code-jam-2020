from django.shortcuts import render
from rest_framework import viewsets
from fbbackend import models, serializers

'''
Views for our Rest API.
We went with class based views, because they were a better fit than functions
'''

class Account_View(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

class Group_View(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

class Message_View(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

class Post_View(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


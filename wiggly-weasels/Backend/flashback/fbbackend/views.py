from django.shortcuts import render
from rest_framework import viewsets
from fbbackend import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

'''
Views for our Rest API.
We went with class based views, because they were a better fit than functions
'''

class Account_View(viewsets.ModelViewSet): #Allow you to view all Accounts and Create New ones
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer

    @action(detail=False, methods=['post'], name='Check Login', url_path='check-login', url_name='check_login')
    def check_login(self, request, pk=None):
        login_serializer = serializers.LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            user = models.Account.objects.get(nickname=login_serializer.data['username'])
            if user.hashed_pass == login_serializer.data['password']:
                return Response({'username': login_serializer.data['username']})
            else:
                return Response({'Authentication': 'Failed'}, status=status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class Group_View(viewsets.ModelViewSet): #Allow you to view all Groups and Create New ones
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    
    @action(detail=False, methods=['post'], name='New Message', url_path='new-message', url_name='new_message')
    def new_message(self, request, pk=None):
        serializer = serializers.MessageSerializer(data=request.data)

        if serializer.is_valid():
            group = models.Group.objects.get(name=serializer.data['group_name'])
            group.messages.append(request.data)
            group.save()

            return Response({'status': 'created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], name='Join Group', url_path='join-group', url_name='join_group')
    def join_group(self, request, pk=None):
        serializer = serializers.JoinSerializer(data=request.data)

        if serializer.is_valid():
            return Response(models.Group.objects.get(serializer.data['group_name']))
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], name='Read Messages', url_path='read-message', url_name='read_messages')
    def read_messages(self, request, pk=None):
        serializer = serializers.ReadSerializer(data=request.data)
        if serializer.is_valid():
            group = models.Group.objects.get(name=serializer.data['group_name'])
            print(group.messages[0:])
            return Response({'messages': group.messages[serializer.data['index']:]})
            
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)









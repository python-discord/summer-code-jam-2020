from django.shortcuts import render
from rest_framework import viewsets
from fbbackend import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import action

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

    @action(detail=False, methods=['post'])
    def new_message(self, request, pk=None):
        group = self.get_object()
        serializer = serializers.MessageSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            group.messages.append(serializer.data)
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)




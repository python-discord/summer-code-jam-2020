# For our views/endpoints
from rest_framework import viewsets  # Viewsets for API Views
from rest_framework.response import Response  # Response Class to return data
from rest_framework.decorators import action  # Decorator to define views
from rest_framework import status  # Returning Status Codes

from fbbackend import models, serializers  # Our models and serializers

# Thx f1re for dedicating so much time to help us
# and the entire events team for keeping our team together after everything that happened <3

'''
Views for our Rest API.
We went with class based views, because they were a better fit than functions
'''


class Account_View(viewsets.ModelViewSet):  # Account Viewset
    queryset = models.Account.objects.all()  # Define Queryset for get requests
    serializer_class = serializers.AccountSerializer  # The account class' main serializer

    @action(detail=False, methods=['post'], name='Check Login', url_path='check-login', url_name='check_login')
    def check_login(self, request, pk=None):  # Function to check the validity of login information
        login_serializer = serializers.LoginSerializer(data=request.data)  # Define serializer to validate info
        if login_serializer.is_valid():  # If the data is valid
            try:
                user = models.Account.objects.get(nickname=login_serializer.data['username'])  # Find account with name
            except models.Account.DoesNotExist:  # The model does not exist
                return Response({'Authentication': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)  # Bad request
            if user.hashed_pass == login_serializer.data['password']:  # Is the password + username correct?
                return Response({'username': login_serializer.data['username']})  # Returns the username
            else:
                return Response({'Authentication': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(login_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class Group_View(viewsets.ModelViewSet):  # Allow you to view all Groups and Create New ones
    queryset = models.Group.objects.all()  # Gets the queryset for the group get request
    serializer_class = serializers.GroupSerializer  # Gets the main "Group" serializer

    @action(detail=False, methods=['post'], name='New Message', url_path='new-message', url_name='new_message')
    def new_message(self, request, pk=None):  # Create a new message
        '''
        parameters:

        GroupName: the name of the group chat
        Sender: The username of the sender of the message
        Content: The contents of the message being sent

        '''
        serializer = serializers.MessageSerializer(data=request.data)  # Create instance to validate data

        if serializer.is_valid():  # If the data is valid
            group = models.Group.objects.get(name=serializer.data['group_name'])  # Get the group using its name
            group.messages.append(request.data)  # Add the data to a list of messages within the group class
            group.save()  # Save the new data

            return Response({'status': 'created'})  # Return the a response with status as "created"
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)  # Return an error

    @action(detail=False, methods=['post'], name='Join Group', url_path='join-group', url_name='join_group')
    def join_group(self, request, pk=None):  # Join a group
        serializer = serializers.JoinSerializer(data=request.data)  # Create serializer to validate data

        '''
        parameters:

        GroupName: the name of the group chat
        '''

        if serializer.is_valid():
            try:
                group = models.Group.objects.get(name=serializer.data['group_name'])  # Get the group data
                return Response({'messages': group.messages, 'creator': group.creator})
            except models.Group.DoesNotExist:  # The group does not exist
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], name='Read Messages', url_path='read-message', url_name='read_messages')
    def read_messages(self, request, pk=None):  # Return list of messages after a specific index requested by client
        serializer = serializers.ReadSerializer(data=request.data)
        if serializer.is_valid():
            group = models.Group.objects.get(name=serializer.data['group_name'])
            return Response({'messages': group.messages[serializer.data['index']:]})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

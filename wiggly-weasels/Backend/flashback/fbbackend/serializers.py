from rest_framework import serializers
from fbbackend import models

'''
Serializers for the "Model" objects located in Models.py
'''


class AccountSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Account
        fields = ('email', 'hashed_pass', 'nickname', 'bot')


class GroupSerializer(serializers.ModelSerializer):  # Serializer for Groups
    class Meta:
        model = models.Group
        fields = ('creator', 'messages', 'name')


class MessageSerializer(serializers.Serializer):
    sender = serializers.CharField()
    content = serializers.CharField()

    group_name = serializers.CharField()


class ReadSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    group_name = serializers.CharField()


class JoinSerializer(serializers.Serializer):
    group_name = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



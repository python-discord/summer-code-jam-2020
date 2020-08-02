from rest_framework import serializers
from fbbackend import models

'''
Serializers for the "Model" objects located in Models.py
'''

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('email', 'hashed_pass', 'identification', 'nickname', 'bot')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ('writer', 'content', 'identification')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('creator', 'identification', 'messages', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('creator', 'content', 'identification', 'title', 'comments')


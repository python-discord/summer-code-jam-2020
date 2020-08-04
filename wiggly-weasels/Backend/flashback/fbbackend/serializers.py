from rest_framework import serializers
from fbbackend import models

'''
Serializers for the "Model" objects located in Models.py
'''

class AccountSerializer(serializers.ModelSerializer): #Serializer for accounts
    class Meta:
        model = models.Account
        fields = ('email', 'hashed_pass', 'nickname', 'bot')



class GroupSerializer(serializers.ModelSerializer): #Serializer for Groups
    class Meta:
        model = models.Group
        fields = ('creator', 'messages', 'name')





from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class Account(models.Model):  # A model containing user information
    '''

    email: The user's email (which they used to sign up)
    hashed_pass: A Hashed Version of their password, so they can login
    identification: A Randomly Generated Unique ID
    nickname: The user's nickname on the IRC and Forum
    bot: A boolean to indicate whether a user is a bot

    '''
    # Technical Information
    email = models.EmailField(max_length=100)
    hashed_pass = models.CharField(max_length=64)

    # Display
    nickname = models.CharField(max_length=20, primary_key=True)
    bot = models.BooleanField(default=False)


class Group(models.Model):
    '''

    creator: creator of the chatroom
    identification: A randomly generated Unique ID
    messages: An array containing a Dictionary:
    {
        "sender": "",
        "content": ""
    }

    name: The name of group

    '''
    creator = models.CharField(max_length=100)  # The ID of the User
    messages = ArrayField(  # ArrayField Containing Messages
        JSONField()

    )
    name = models.CharField(max_length=20, primary_key=True)

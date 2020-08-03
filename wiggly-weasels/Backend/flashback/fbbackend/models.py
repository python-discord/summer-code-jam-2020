from django.db import models
from uuid import uuid4
from django.contrib.postgres.fields import ArrayField


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
    messages: An array containing an array for each message.
        ar[0] = Name
        ar[1] = Content
    name: The name of group

    '''
    creator = models.CharField(max_length=100)  # The ID of the User
    messages = ArrayField(  # ArrayField Containing Messages
        ArrayField(
            models.CharField(max_length=1000),
            size=2
        )
    )

    name = models.CharField(max_length=20, primary_key=True)


class Post(models.Model):
    '''

    creator: The user who posts the thread
    identification: A randomly generated Unique ID
    comments: An array containing an array for each message.
        ar[0] = Commenter ID
        ar[1] = Content
    title: The title of the thread

    '''

    identification = models.CharField(max_length=100, default=uuid4().hex, blank=True, primary_key=True)
    creator = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    title = models.CharField(max_length=35)

    comments = ArrayField(  # ArrayField Containing Messages
        ArrayField(
            models.CharField(max_length=1000),
            size=2
        )
    )

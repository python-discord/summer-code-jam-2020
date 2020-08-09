from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Use this dictionary to define attributes of fields that need to be referenced elsewhere, for example in validation
# Key's should be in the format <table name>__<field name>__<attribute>
_model_field_limits = {
    'ChatRoom__name__max_length': 20,
    'Message__message__max_length': 250
}


class ChatRoom(models.Model):
    name = models.CharField(max_length=_model_field_limits['ChatRoom__name__max_length'])


class ChatMessage(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    chat_room_id = models.ForeignKey(ChatRoom, null=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField()
    message = models.CharField(max_length=_model_field_limits['Message__message__max_length'])
    parent_message_id = models.IntegerField(null=True)

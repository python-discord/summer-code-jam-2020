from .models import Message
from .models import Room
from .models import SimpleUser
from typing import List
from typing import NoReturn
from django.utils import timezone


def get_messages_for_room(room: Room) -> List[str, ...]:
    """
    Gets a list of messages for a given room.

    :param room: A room.
    :return: A list of messages for the room.
    """

    messages = []

    for message in Message.objects.filter(room__eq=room):
        # TODO: How do we want to format the time?
        messages.append(f'{message.sender} at {message.created_at}: {message.text}')

    return messages


def create_message(room: Room, sender: SimpleUser, time: timezone, text: str) -> Message:
    """
    Creates a message.

    :param room: The room in which the message was sent.
    :param sender: The sender of the message.
    :param time: The time at which the message was created.
    :param text: The message content.
    """
    return Message(room=room, sender=sender, created_at=time, text=text)


def save_message_to_database(message: Message) -> NoReturn:
    """
    Saves a message to the database.

    :param message: The message to save to the database.
    """

    message.save()

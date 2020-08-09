from chat.models import SimpleUser
from chat.models import Room
import typing


def username_is_available(username: str) -> bool:
    """
    Checks if the given username is available.
    If the username is available, it's not tied to any user in the users table.

    :param username: A screen name.
    :return: True if the screen name is available, false otherwise.
    """

    # Fetch all users from the users table with the same screen name.
    # If there are no users with the same name, then the first item of the result will be none.
    return SimpleUser.objects.filter(username=username).first() is None


def add_user(username: str, room: Room) -> typing.NoReturn:
    """
    Adds a user to the users table.

    :param username: The user's username
    :param room: The room the user is in
    """

    # Create and save the user to the database.
    SimpleUser(username=username, room=room).save()


def remove_user(username: str) -> typing.NoReturn:
    """
    Removes a user from the users table.

    :param username: The username of the user to remove.
    """

    # Remove the user with the matching username.
    SimpleUser.objects.remove(username=username)


def move_user(username: str, to_room: Room) -> typing.NoReturn:
    """
    Moves a user to the specified room.

    :param username: The user's username.
    :param to_room: The room to which the user should be moved
    """

    # Get the user with the matching username and update their room.
    SimpleUser.objects.filter(username=username).update(room=to_room)

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

    # Create the user
    user = SimpleUser(username=username, room=room)

    # Save the user to the database
    user.save()

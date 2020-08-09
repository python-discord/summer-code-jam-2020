from typing import Optional

from .models import Message, Room


class RoomService:
    """Service for manipulating with instances of Room model."""
    @staticmethod
    def get_room_by_id(room_id: int) -> Optional[Room]:
        """Returns room by its id if it exists else return None."""
        try:
            return Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return None


class MessageService:
    """Service for manipulating with instances of Message model."""
    @staticmethod
    def get_distinct_messages(room_id: int):
        """Returns distinct text values ordered by created_at of messages from database."""
        return [item["text"] for item in
            Message.objects.filter(room_id=room_id).order_by('created_at').values('text', 'created_at').distinct()]

    @staticmethod
    def get_all():
        """Returns all instances of message."""
        return Message.objects.order_by('created_at')

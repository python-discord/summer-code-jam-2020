from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from shiny_sheep.games.api.serializers import RoomSerializer
from shiny_sheep.games.models import Room


class RoomCreateView(APIView):
    """View to create a Room"""
    permission_classes = [AllowAny]

    def post(self, request):
        """Creates a Room object with the given data"""
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    """The view that handles requests to do get/delete Rooms"""
    permission_classes = [AllowAny]

    def get_object(self, game_id):
        try:
            return Room.objects.get(game_id=game_id)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, game_id):
        """Returns the JSON representation of a Room by game_id"""
        room = self.get_object(game_id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def delete(self, request, game_id):
        room = self.get_object(game_id)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

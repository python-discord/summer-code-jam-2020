from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from shiny_sheep.chat.api.serializers import RoomSerializer
from shiny_sheep.chat.models import Room
from shiny_sheep.users.models import User


class RoomCreateView(APIView):
    """View to create a Room"""
    permission_classes = [AllowAny]

    def get_object(self, name):
        """Get a Room by name"""
        try:
            return Room.objects.get(name=name)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request):
        """Returns the JSON representation of a Room by name"""
        room_name = request.query_params.get('name')
        room = self.get_object(room_name)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def post(self, request):
        """Creates a Room object with the given data"""
        data = {
            'name': request.data['name'],
            'owner': User.objects.filter(username=request.data.get('owner')).first()
        }
        if data['owner'] is not None:
            data['owner'] = data['owner'].pk
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    """The view that handles requests to do get/delete Rooms"""
    permission_classes = [AllowAny]

    def get_object(self, pk):
        """Get a Room from pk"""
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """Returns the JSON representation of a Room by pk"""
        room = self.get_object(pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Delete a room by pk"""
        room = self.get_object(pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shiny_sheep.games.api.serializers import RoomSerializer
from shiny_sheep.games.models import Room


@api_view(['GET', 'POST', 'DELETE'])
def api_detail_room_view(request, slug):
    pass

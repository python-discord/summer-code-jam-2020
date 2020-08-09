from django.http import JsonResponse, HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.utils import json

from tictactoe.tictactoe import TicTacToe

tictactoe = None


@api_view(['POST'])
def start_playing(request):
    data = json.loads(request.body)
    global tictactoe
    tictactoe = TicTacToe(data['turn'])
    return HttpResponse('ok')


@api_view(['GET'])
def get_preview(request):
    data = tictactoe.preview()
    preview = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            preview[f'{i}{j}'] = data[i][j]
    return JsonResponse(preview)


@api_view(['POST'])
def make_move(request):
    data = json.loads(request.body)
    winner = tictactoe.make_move(data['x'], data['y'])
    return JsonResponse({'winner': winner}, safe=False)

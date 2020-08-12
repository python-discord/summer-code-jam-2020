from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from core.helpers import jsonbody
from games.tictactoe import play_game

TIC_TAC_TOE_SCHEMA = {
    'type': 'object',
    'required': ['player', 'board', 'move'],
    'properties': {
        'player': {
            'type': 'string',
            'enum': ['X', 'O'],
        },
        'board': {
            'type': 'array',
            'items': {
                'type': ['string', 'null'],
                'enum': ['X', 'O', None],
            },
        },
        'move': {
            'type': 'integer',
            'enum': list(range(9)),
        },
    },
}


@login_required
@jsonbody(TIC_TAC_TOE_SCHEMA)
def make_move(request, data):
    board, over, score = play_game(data['board'], data['player'], data['move'])
    return JsonResponse({'board': board, 'game_over': over, 'score': score})

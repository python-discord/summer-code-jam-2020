import json
from unittest.mock import patch
from django.test import TestCase, Client
from django.contrib.auth.models import User

from games.tictactoe import play_game


class TicTacToeTest(TestCase):

    @patch('games.views.play_game')
    def test_make_move(self, play):
        play.return_value = 'board', 'over', 'score'
        User.objects.create_user('bla', password='test')

        client = Client()
        client.login(username='bla', password='test')

        res = client.post('/api/games/ttt', json.dumps({
            'player': 'X',
            'move': 3,
            'board': ['X', None, None,
                      'O', None, None,
                      None, None, None],
        }), content_type='application/json')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            json.loads(res.content.decode()),
            {'board': 'board', 'game_over': 'over', 'score': 'score'},
        )

    def test_play_start(self):
        board_start = [
            None, None, None,
            None, None, None,
            None, None, None,
        ]
        board, game_over, score = play_game(board_start, 'X', 0)
        self.assertEqual(board, [
            'X', None, None,
            None, None, None,
            None, None, 'O',
        ])
        self.assertFalse(game_over)
        self.assertEqual(score, 0)

    def test_player_wins(self):
        board_start = [
            'X', None, None,
            'O', 'X', None,
            None, 'O', None,
        ]
        board, game_over, score = play_game(board_start, 'X', 8)
        self.assertEqual(board, [
            'X', None, None,
            'O', 'X', None,
            None, 'O', 'X',
        ])
        self.assertTrue(game_over)
        self.assertEqual(score, 1)

    def test_play_defensive(self):
        board_start = [
            'X', 'O', None,
            None, None, None,
            None, None, None,
        ]
        board, game_over, score = play_game(board_start, 'X', 3)
        self.assertEqual(board, [
            'X', 'O', None,
            'X', None, None,
            'O', None, None,
        ])
        self.assertFalse(game_over)
        self.assertEqual(score, 0)

    def test_play_offensive(self):
        board_start = [
            'X', None, None,
            'X', None, None,
            'O', None, 'O',
        ]
        board, game_over, score = play_game(board_start, 'X', 2)
        self.assertEqual(board, [
            'X', None, 'X',
            'X', None, None,
            'O', 'O', 'O',
        ])
        self.assertTrue(game_over)
        self.assertEqual(score, -1)

import json
from unittest.mock import patch
from django.test import TestCase, Client
from chat.models import User


class ChatLobbyTest(TestCase):

    @patch('chat.views.check_chat_room_name')
    def test_invalid_names(self, data):
        User.objects.create_user('fake', password='test')

        client = Client()
        client.login(username='fake', password='test')

        tests = [
            ('', 400, None),
            ('hello!', 200, {"valid": False, "message": "Invalid chat room name. Names must be alphanumeric."}),
            ('fartoolonganame' * 10, 400, None)
        ]

        for (invalid_name, expected_status_code, content) in tests:
            res = client.post('/api/chat/checkname/', json.dumps({
                'roomName': invalid_name
            }), content_type='application/json')

            self.assertEqual(res.status_code, expected_status_code)
            if content:
                self.assertEqual(
                    json.loads(res.content.decode()),
                    content,
                )

    @patch('chat.views.check_chat_room_name')
    def test_valid_names(self, data):
        User.objects.create_user('fake', password='test')

        client = Client()
        client.login(username='fake', password='test')

        tests = [
            ('myroom', 200, {"valid": True, "message": "Ok"}),
            ('myRoom', 200, {"valid": True, "message": "Ok"}),
            ('123', 200, {"valid": True, "message": "Ok"}),
            ('HowRU111', 200, {"valid": True, "message": "Ok"})
        ]

        for (valid_name, expected_status_code, content) in tests:
            res = client.post('/api/chat/checkname/', json.dumps({
                'roomName': valid_name
            }), content_type='application/json')

            self.assertEqual(res.status_code, expected_status_code)
            if content:
                self.assertEqual(
                    json.loads(res.content.decode()),
                    content,
                )

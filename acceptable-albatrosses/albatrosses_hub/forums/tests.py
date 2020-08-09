from datetime import datetime
from django.urls import reverse
from django.test import TestCase, Client, RequestFactory
from .models import Board, Post
from ..authentication.models import User
from .views import PostCreateView, CommentCreateView, BoardCreateView


class ForumTestCase(TestCase):
    """Class to perform unit tests of forum app."""

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="tester",
            email="test@example.com",
            password="tester12345"
        )

        self.board = Board(
            name="Test",
            description="This is testing."
        )
        self.board.save()

        self.post = Post(
            subject="subject_test",
            message="message_test",
            board=self.board,
            created_at=datetime.now(),
            created_by=self.user,
        )
        self.post.save()

    def test_forum_url(self):
        response = Client().get(reverse("forums-home"))
        self.assertEqual(response.status_code, 200)

    def test_forum_create_board_url(self):
        response = Client().get(reverse("board-create"))
        self.assertIn(response.status_code, (200, 302))

    def test_forum_board_url(self):
        response = Client().get(reverse("board-view", args=["Test"]))
        self.assertEqual(response.status_code, 200)

    def test_forum_create_post_url(self):
        response = Client().get(reverse("post-create", args=["Test"]))
        self.assertIn(response.status_code, (200, 302))

    def test_forum_post_list_url(self):
        response = Client().get(reverse("board-detail", args=["Test", 1]))
        self.assertEqual(response.status_code, 200)

    def test_forum_update_post_url(self):
        response = Client().get(reverse("post-update", args=["Test", 1]))
        self.assertIn(response.status_code, (200, 302))

    def test_forum_delete_post_url(self):
        response = Client().get(reverse("post-delete", args=["Test", 1]))
        self.assertIn(response.status_code, (200, 302))

    def test_forum_create_comment_url(self):
        response = Client().get(reverse("comment-create", args=["Test", 1]))
        self.assertIn(response.status_code, (200, 302))

    def test_forum_update_comment_url(self):
        response = Client().get(reverse("comment-update", args=["Test", 1, 1]))
        self.assertIn(response.status_code, (200, 302))

    def test_forum_delete_comment_url(self):
        response = Client().get(reverse("comment-delete", args=["Test", 1, 1]))
        self.assertIn(response.status_code, (200, 302))

    def test_user_post_list_url(self):
        response = Client().get(reverse("user-posts", args=["tester"]))
        self.assertEqual(response.status_code, 200)


class ForumViewTest(TestCase):
    """Class to perform some tests related to views."""

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="tester",
            email="test@example.com",
            password="tester12345"
        )

        self.board = Board(
            name="Test",
            description="This is testing."
        )
        self.board.save()

        self.post = Post(
            subject="subject_test",
            message="message_test",
            board=self.board,
            created_at=datetime.now(),
            created_by=self.user,
        )
        self.post.save()

    def test_post_create_view_context(self):
        request = self.factory.get(reverse("post-create", args=["Test"]))
        request.user = self.user
        response = PostCreateView.as_view()(request)

        self.assertIsNotNone(response.context_data["login"])
        self.assertIsNotNone(response.context_data["page"])

    def test_comment_create_view_context(self):
        request = self.factory.get(reverse("comment-create", args=["Test", 1]))
        request.user = self.user
        response = CommentCreateView.as_view()(request)

        self.assertIsNotNone(response.context_data["login"])
        self.assertIsNotNone(response.context_data["page"])

    def test_get_success_url_from_board_create_view(self):
        response = BoardCreateView.get_success_url(object)
        self.assertEqual(response, reverse("forums-home"))

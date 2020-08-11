from django.test import TestCase

from .models import ForumPost


class PostCreation(TestCase):

    def setUp(self):
        ForumPost.objects.create(
            title="Dancing Pelicans",
            author="Peliman",
            description="A Dancing Pelican")

    def ReplyCreationTest(self):
        post = ForumPost.objects.get(author="Peliman")
        post.forumpostreply_set.create(
            author="Pelicant",
            content="He's just eating")

        self.assertEquals(len(post.forumpostreply_set.all()), 1)
        self.assertEquals(post.forumpostreply_set.all()[0].author, "Peliman")

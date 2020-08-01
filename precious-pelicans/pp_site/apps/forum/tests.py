from django.test import TestCase
from .models import ForumPostOriginal
from django.utils import timezone


class PostCreation (TestCase):

    def setUp(self):
        ForumPostOriginal.objects.create(
            date=timezone.now(),
            title="Dancing Pelicans",
            author="Peliman",
            description="A Dancing Pelican")

    def ReplyCreationTest(self):
        post = ForumPostOriginal.objects.get(author="Peliman")
        post.forumpostreply_set.create(
            date=timezone.now(),
            author="Pelicant",
            content="He's just eating")

        self.assertEquals(len(post.forumpostreply_set.all()), 1)
        self.assertEquals(post.forumpostreply_set.all()[0].author, "Peliman")

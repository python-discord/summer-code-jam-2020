from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import Truncator

# Create your models here.


class Board(models.Model):
    """
    Class for message boards.
    """

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __repr__(self):
        cls = self.__class__.__name__
        return f"<{cls}: name={self.name!r} description={self.description!r}>"

    def __str__(self):
        return self.name

    def get_comments_count(self):
        """
        returns number of comments belonging to the board.
        """
        return Comment.objects.filter(post__board=self).count()

    def get_last_comment(self):
        """
        return the last comment belonging to the board.
        """
        return Comment.objects.filter(post__board=self).order_by("-created_at").first()


class Post(models.Model):
    """
    Class for post
    """

    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=4000)
    board = models.ForeignKey(Board, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name="create_by", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name="+", on_delete=models.CASCADE)

    def __repr__(self):
        cls = self.__class__.__name__
        return f"<{cls}: board={self.board!r} subject={self.subject!r} \
                created_by={self.created_by!r} updated_at={self.updated_at!r} \
                content={self.message!r}>"

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        """
        returns url to post
        """
        return reverse("forums:board-detail", kwargs={"board": self.board.name, "pk": self.pk})


class Comment(Post):
    """
    Class for comments
    """

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

    def get_absolute_url(self):
        """
        returns url to post
        """
        return reverse(
            "forums:comment-detail", kwargs={"board": self.post.board.name, "post_pk": self.post.pk, "pk": self.pk}
        )

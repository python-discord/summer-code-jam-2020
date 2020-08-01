from django.db import models
from users.models import Profile

# Migrations have not been run yet until Likes model is completed


class Post(models.Model):
    """
    Model for the Blog posts that every user should be able to posts
    """

    title = models.CharField(max_length=300, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    date_published = models.DateTimeField(auto_now_add=True)

    @property
    def likes(self):
        # should return the number of Likes objects belonging to this Comment
        return


class Comment(models.Model):
    """
    A model that has number of likes, a foreign key to author,
    and a foreign key to the Post it is for.
    """

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    @property
    def likes(self):
        # should return the number of Likes objects belonging to this Comment
        return


class Likes(models.Model):
    """
    OneToOne to both the object (post/comment) that was liked,
    and also the user who liked the object
    (may need a related_name)
    """

    pass

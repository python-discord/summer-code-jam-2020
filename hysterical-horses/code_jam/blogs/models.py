from django.db import models
from .users.models import Profile
# I have no idea if this import is going to work or not
# Migrations have not been run yet until Likes model is completed


class Post(models.Model):
    """
    Model for the Blog posts that every user should be able to posts
    """

    title = models.CharField(max_length=300, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title  # or self.content


class Comment(models.Model):
    """
    A model that has number of likes, a foreign key to author,
    and a foreign key to the Post it is for.
    """

    # Not quite sure what models.ForeignKey is. Apologies if its all wrong.
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)


class Likes(models.Model):
    """
    OneToOne to both the object (post/comment) that was liked,
    and also the user who liked the object
    (may need a related_name)
    """

    pass

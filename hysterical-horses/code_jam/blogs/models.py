from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    """
    Model for the Blog posts that every user should be able to posts
    """

    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=300, blank=False, null=False, unique=True)
    content = models.TextField(blank=False, null=False)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    @property
    def likes(self):
        return len(self.all_likes.all())

    class Meta:
        ordering = ('author__username',)


class Comment(models.Model):
    """
    A model that has number of likes, a foreign key to author,
    and a foreign key to the Post it is for.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="author")
    content = models.CharField(max_length=250, blank=False, null=False)
    # content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True,
                               blank=True, related_name="replies")

    def __str__(self):
        return self.post.title + ' | ' + self.author.username

    class Meta:
        ordering = ('-created',)


class Like(models.Model):
    """
    Likes for posts, owned by both the post and the user
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="all_likes")

    def __str__(self):
        return self.post.title

    def can_like(self):
        is_own_post = self.post.title in [x.title for x in self.author.posts.all()]
        already_liked = self.post.title in [x.post.title for x in self.author.all_likes.all()]
        return not is_own_post and not already_liked

    def save(self, *args, **kwargs):
        if self.can_like():
            super().save(*args, **kwargs)

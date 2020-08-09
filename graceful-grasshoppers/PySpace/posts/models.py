from django.db import models
from django.utils import timezone
from users.models import CustomUser
from api.models import File


class Like(models.Model):
    """A model for the likes a post got"""

    date_liked = models.DateTimeField(default=timezone.now)
    user_liked = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_liked}'s like"


class Dislike(models.Model):
    """A model for the dislikes a post got"""

    date_disliked = models.DateTimeField(default=timezone.now)
    user_disliked = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_disliked}'s dislike"


class Post(models.Model):
    """A model for the post a user makes"""

    title = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    likes = models.ManyToManyField(Like, blank=True)
    dislikes = models.ManyToManyField(Dislike, blank=True)

    post_image = models.ForeignKey(File, null=True, on_delete=models.CASCADE)

    def __lt__(self, val):
        return self.date_posted < val.date_posted

    def __str__(self):
        return f"{self.title} by {self.author}"


class PostComment(models.Model):
    content = models.TextField(default="")
    user_commented = models.ForeignKey(CustomUser, models.CASCADE, related_name="commenting_user")
    post = models.ForeignKey(Post, models.CASCADE, related_name="post_commented_on")

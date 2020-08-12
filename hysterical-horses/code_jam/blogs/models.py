from django.db import models
from django.conf import settings
from django.urls import reverse


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    """
    Model for the Blog posts that every user should be able to posts
    """

    author = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=300, blank=False, null=False, unique=True)
    content = models.TextField(blank=False, null=False)
    date_published = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts_likes")

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ("author__username",)


class Comment(models.Model):
    """
    A model that has number of likes, a foreign key to author,
    and a foreign key to the Post it is for.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=250, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    def __str__(self):
        inner = ", ".join(
            [self.post.title, self.author.username, self.content, str(self.parent)]
        )
        rv = " ".join(["<Comment", inner, ">"])
        return rv

    class Meta:
        ordering = ("-created",)

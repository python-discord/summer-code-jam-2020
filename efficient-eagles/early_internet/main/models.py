from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to="profile_imgs/", null=True)
    bio = models.TextField(
        max_length=100, default="Hi, I am a HoneyFeed User", null=True
    )

    def __str__(self):
        return self.username


class Topic(TimeStampedModel):
    name = models.CharField(max_length=20, default="", blank=False, unique=True)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=255, default="", blank=True)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    body = models.TextField(default="", blank=True)

    slug = models.SlugField(max_length=255, default="", blank=True, unique=True)

    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    @property
    def url(self):
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse("topic", slug=self.slug)

    @property
    def comment_url(self):
        return "{}/comments/".format(self.slug)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save()
        if not self.slug:
            slug = slugify(self.title)
            try:
                slug += "-" + str(self.id)
            except Post.DoesNotExist:
                pass
            self.slug = slug
            self.save()


class Comment(TimeStampedModel):
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    body = models.CharField(max_length=10000, default="")

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_thread = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
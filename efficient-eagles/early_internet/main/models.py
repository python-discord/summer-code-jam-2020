from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to ='profile_imgs/', null=True)
    bio = models.TextField(max_length=100, default='Hi, I am a HoneyFeed User')

    def __str__(self):
        return self.username


class Post(TimeStampedModel):
    title = models.CharField(max_length=255,
                             default='',
                             blank=True)

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    body = models.TextField(default='',
                            blank=True)

    slug = models.SlugField(max_length=255,
                            default='',
                            blank=True,
                            unique=True)

    models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    @property
    def url(self):
        return '{}'.format(self.id)

    @property
    def comment_url(self):
        return '/comments/{}'.format(self.id)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Topic(TimeStampedModel):
    pass


class Comment(TimeStampedModel):
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    body = models.CharField(max_length=10000, default='')
    
    author = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    comment_thread = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

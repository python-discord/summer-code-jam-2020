from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from users.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)


class BlogComment(Comment):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)


class ProfileComment(Comment):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)

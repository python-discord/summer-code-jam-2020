from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50)
    gender = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(null=True, max_length=2, help_text="ISO 639 country code.")
    city = models.CharField(null=True, max_length=50)
    date_of_birth = models.DateField(null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


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

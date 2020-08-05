from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)
    join_date = models.DateTimeField()


class Community(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    subscribers = models.ManyToManyField(User)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

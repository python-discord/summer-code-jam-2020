from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='img/users/avatar')
    join_date = models.DateTimeField()


class Community(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_owner')
    admin = models.ManyToManyField(User, related_name='community_admin')
    subscribers = models.ManyToManyField(User, related_name='community_subscribers')
    location = models.CharField(max_length=20)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    publisher = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='post_publisher')
    title = models.CharField(max_length=100)
    description = models.TextField()
    views = models.ManyToManyField(User)
    creation_date = models.DateTimeField()


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    content = models.TextField()
    creation_date = models.DateTimeField()

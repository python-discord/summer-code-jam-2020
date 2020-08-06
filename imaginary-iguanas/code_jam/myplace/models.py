from django.db import models

from users.models import Profile


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'BlogPost {self.title} : {self.description}'


class Comment(models.Model):
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.user.username} content: {self.comment}'


class BlogComment(Comment):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)


class ProfileComment(Comment):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')

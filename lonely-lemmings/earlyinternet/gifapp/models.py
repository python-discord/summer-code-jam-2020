from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    date_created = models.DateField(auto_now_add=True)


class Image(models.Model):
    image_name = models.CharField(max_length=50)
    image_path = models.ImageField(upload_to='')  # add path accordingly


class Project(models.Model):
    name = models.CharField(max_length=100)
    author = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=1300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    picture = models.ForeignKey(Image)
    gif_bool = models.BooleanField(default=False)  # use false for static, true for gif


class Comment(models.Model):
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)

# class GifProject(Project):
#     image_list = None
#     image_gif = None
#
#     def __str__(self):
#         pass
#
#     def compile_images(self):
#         pass

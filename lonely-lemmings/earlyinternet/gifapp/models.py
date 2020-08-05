from django.db import models
from djrichtextfield.models import RichTextField


class User(models.Model):
    """represents an app user"""
    registration_date = models.DateTimeField()
    profile_picture = models.ImageField()

    def __str__(self):
        pass


class ProjectType(models.Model):
    """represents a possible project type out of gif and still"""
    GIF = "GIF"
    IMG = "IMG"

    PROJECT_TYPES = (
        (GIF, 'gif project'),
        (IMG, 'image project')
    )

    project_type = models.CharField(max_length=25, choices=PROJECT_TYPES)


class Project(models.Model):
    """represents a project that an user can do, can either be a gif or still image project"""
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    preview_version = models.ImageField()
    upload_version = models.ImageField()

    def __str__(self):
        pass


class Image(models.Model):
    """represents an image that can be inside a project"""
    project_id = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50)
    image_data = models.ImageField()
    date_created = models.DateTimeField()
    date_last_modified = models.DateTimeField()

    def __str__(self):
        pass


class Post(models.Model):
    """represents a post that can be added to a feed"""
    title = models.TextField(max_length=50)
    project_id = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)

    def __str__(self):
        pass


class Comment(models.Model):
    """represents a comment on a post or another comment"""
    content = RichTextField()
    post_id = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        pass

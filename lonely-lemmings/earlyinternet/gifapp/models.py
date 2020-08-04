from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    author = None
    date_created = models.DateTimeField()
    date_last_modified = None
    picture = None

    class Meta:
        abstract = True

    def get_absolute_url(self):
        pass


class GifProject(Project):
    image_list = None
    image_gif = None

    def __str__(self):
        pass

    def compile_images(self):
        pass


class ImageProject(Project):
    def __str__(self):
        pass


class Image(models.Model):
    project = None
    image_name = models.CharField(max_length=50)
    image_data = models.ImageField()

    def __str__(self):
        pass


class User(models.Model):
    projects = None
    registration_date = None

    def __str__(self):
        pass

    def new_project(self):
        pass

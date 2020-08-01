from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Template(models.Model):
    name = models.CharField(max_length=80)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    style_sheet = models.FileField(null=False, blank=False, upload_to='styles/')


def user_directory_path(instance, filename):
    return f'thumbnails/{instance.name}/{filename}'


class Webpage(models.Model):
    name = models.CharField(max_length=80)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='thumbnails/')
    template_used = models.ForeignKey(Template, on_delete=models.DO_NOTHING)
    votes = models.IntegerField(default=0)

    user_title = models.CharField(max_length=100, verbose_name='page title')
    user_text_1 = models.TextField(verbose_name='subtitle paragraph')
    user_text_2 = models.TextField(verbose_name='main body paragraph')
    user_text_3 = models.TextField(verbose_name='closing paragraph')

    # todo: make sure background images repeat/tessellate in css if a background image is uploaded
    user_image_1 = models.ImageField(
        null=True, blank=True, upload_to=user_directory_path, verbose_name='background image')
    user_image_2 = models.ImageField(
        null=True, blank=True, upload_to=user_directory_path, verbose_name='header image')
    user_image_3 = models.ImageField(
        null=True, blank=True, upload_to=user_directory_path, verbose_name='main image')
    user_image_4 = models.ImageField(
        null=True, blank=True, upload_to=user_directory_path, verbose_name='footer image')

    # todo: for tameTNT's reference: https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/


class Comment(models.Model):
    parent_page = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)

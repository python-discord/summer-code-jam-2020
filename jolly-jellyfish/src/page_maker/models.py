from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension
from django.db import models
from django.utils import timezone
from relativefilepathfield.fields import RelativeFilePathField


def get_theme_path():
    return str(Path(settings.BASE_DIR) / 'static')


class Template(models.Model):
    name = models.CharField(max_length=80)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # todo: option to upload own stylesheet rather than select from existing
    #  potentially upload to user_themes within static not media? -
    #  makes finding easier below in RelativeFilePathField
    # style_sheet = models.FileField(null=False, blank=False,
    #                      upload_to='themes/', validators=[FileExtensionValidator(['css'])])

    # model.FilePathField() does not have a url attribute,
    # so accessing the files within a html template is awkward.
    # Using RelativeFilePathField allows for using django static support easily within the template

    # match uses regex applied to base filename only(.*=any characters, \.=., $=end of string)
    style_sheet = RelativeFilePathField(path=get_theme_path, recursive=True, match='.*\.css$')

    def __str__(self):
        return self.name


def get_user_dir_path(instance, filename):
    return f'images/{instance.author.username}/{filename}'


class Webpage(models.Model):
    name = models.CharField(max_length=80, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # todo: default to imgkit generated thumbnail
    thumbnail = models.ImageField(null=True, blank=True, default=None,
                                  upload_to='thumbnails/',
                                  validators=[validate_image_file_extension])
    template_used = models.ForeignKey(Template, on_delete=models.DO_NOTHING)
    votes = models.IntegerField(default=0)

    user_title = models.CharField(max_length=100, verbose_name='page title')
    user_text_1 = models.TextField(verbose_name='subtitle paragraph')
    user_text_2 = models.TextField(verbose_name='main body paragraph')
    user_text_3 = models.TextField(verbose_name='closing paragraph')

    # todo: support for background images with custom templates
    user_image_1 = models.ImageField(
        null=True, blank=True, verbose_name='header image', max_length=200,
        upload_to=get_user_dir_path, validators=[validate_image_file_extension])
    user_image_2 = models.ImageField(
        null=True, blank=True, verbose_name='main image', max_length=200,
        upload_to=get_user_dir_path, validators=[validate_image_file_extension])
    user_image_3 = models.ImageField(
        null=True, blank=True, verbose_name='footer image', max_length=200,
        upload_to=get_user_dir_path, validators=[validate_image_file_extension])

    def was_created_recently(self):
        pass

    def __str__(self):
        return self.name


class Comment(models.Model):
    parent_page = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

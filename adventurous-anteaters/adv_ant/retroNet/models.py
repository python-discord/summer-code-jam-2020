from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, null=True, max_length=100)

    def __str__(self):
        return f"{self.title}"


class UpdateProfile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    about = models.CharField(max_length=200)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

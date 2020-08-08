from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """
    The model to store Posts created by users.
    Fields-
    post_content: The text of the post
    posted_by: User who created the post
    post_date_posted: Date of making the post
    """

    post_content = models.TextField(verbose_name="content")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date_posted = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Published on")
    post_image = models.ImageField(upload_to="images/", blank=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

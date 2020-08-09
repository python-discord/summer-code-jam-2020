from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    """
    The model to store Posts created by users.
    Fields-
    post_content: The text of the post
    posted_by: User who created the post
    post_date_posted: Date of making the post
    post_image: Image posted with the post
    """

    post_content = models.TextField(verbose_name="content")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date_posted = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Published on")
    post_image = models.ImageField(upload_to="post_images", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, **kwargs):
        """
        This function will resize and add a pixelating effect to the images
        to give them a more retro and early internet feel.
        """
        super().save()
        try:
            img = Image.open(self.post_image.path)
        except ValueError as E:
            print("No image was attached with the post\n", repr(E))
            return None
        img = img.resize((240, 240), resample=Image.BILINEAR)

        output_size = (240, 240)
        img = img.resize(output_size, Image.NEAREST)
        img.thumbnail(output_size)
        img.save(self.post_image.path)

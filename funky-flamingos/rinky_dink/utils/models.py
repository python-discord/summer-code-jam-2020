from django.db import models


class File(models.Model):
    title = models.CharField(max_length=255, blank=True)
    hash_val = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Title: {self.title} hash_val :{self.hash_val} uploaded_at {self.uploaded_at}"

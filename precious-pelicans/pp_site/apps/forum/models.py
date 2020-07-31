from django.db import models
from pathlib import Path

# Placeholder until we decide how to serve images/video
class MediaFile (models.Model):
    # The actual file data
    data = models.FileField()
    # Links it to the forum post presented to end users
#    attachedPost = models.OneToOneField(ForumPostOriginal, on_delete=models.CASCADE, primary_key=True)
    # True if media file is a video, false if image
    isVideo = models.BooleanField()

# Top-level post containing the media
class ForumPostOriginal (models.Model):
    # Post title (might not be needed)
    title = models.CharField(max_length=100)
    # Date of publication
    date = models.DateTimeField()
    # Simple username, can swap to a user model with credentials
    author = models.CharField(max_length=30)
    # A description of the media
    description = models.TextField(blank=False)
    # The post's associated media
#    content = models.OneToOneField(MediaFile, on_delete=models.CASCADE, primary_key=False)

# Reply to a top-level post
class ForumPostReply (models.Model):
    # Date of publication
    date = models.DateTimeField()
    # Simple username, can swap to a user model with credentials
    author = models.CharField(max_length=30)
    # Text content of the reply
    content = models.TextField()
    # Links to the post being replied to
    topic = models.ForeignKey(ForumPostOriginal, on_delete=models.CASCADE)
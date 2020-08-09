from django.db import models
from django.contrib.auth.models import User
from chat.models import Room
from PIL import Image
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    background = models.ImageField(upload_to="background")
    status = models.CharField(default=":-)", max_length=100)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ChatRoomVisit(models.Model):
    chat_room = models.ForeignKey(Room, blank=True, null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    time_visited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.chat_room}, {self.profile}, {self.time_visited}"


class FriendRequest(models.Model):
    from_user = models.ForeignKey(Profile, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name="to_user", on_delete=models.CASCADE)

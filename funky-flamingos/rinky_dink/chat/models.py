from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.db.models.signals import pre_save
# from django.utils.text import slugify


class Messages(models.Model):
    # slug = models.SlugField(unique=True, blank=True)
    message = models.CharField(max_length=500, default="")
    time = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")

    def __str__(self):
        return f"{self.sender} sent '{self.message}' on {self.time}"


# class Chat(models.Model):
#     slug = models.SlugField(unique=True, blank=True)
#     message = models.ForeignKey(Messages, on_delete=models.CASCADE)
#     recipent = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.recipent}"

#     def get_absolute_url(self):
#         return reverse("chat_index", kwargs={"slug": self.slug})


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.recipent.username)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Chat.objects.filter(slug=slug).order_by("-id")
#     if qs.exists():
#         new_slug = "%s%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_chat(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)


# pre_save.connect(pre_save_chat, sender=Chat)

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User as AuthUser


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='img/users/avatar', blank=True, null=True)
    join_date = models.DateTimeField(auto_now=True)
    parent = models.OneToOneField(AuthUser, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return '/user/' + str(self.id)

    def __str__(self):
        return self.name


class Community(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_owner')
    admin = models.ManyToManyField(User, related_name='community_admin')
    subscribers = models.ManyToManyField(User, related_name='community_subscribers')
    location = models.CharField(max_length=20)

    def get_absolute_url(self):
        return f'/community/{self.name}/'

    def __str__(self):
        return self.name

    def get_room_id(self):
        return ''.join(word for word in self.name if word.isalnum())


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    publisher = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='post_publisher')
    title = models.CharField(max_length=100)
    description = models.TextField()
    views = models.ManyToManyField(User, blank=True)
    creation_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/community/{self.publisher}/{self.id}/'

    def get_short_intro(self):
        if len(self.description) <= 200:
            return self.description
        else:
            intro = self.description[:200]
            separator = max((intro.rfind(" "), intro.rfind("\n")))
            return intro[:separator]


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)


def create_profile(sender, **kwargs):  # noqa
    if kwargs['created']:
        AuthUser.objects.create_user(
            username=kwargs['instance']
            .name, password=kwargs['instance']
            .password, is_staff=True)


post_save.connect(create_profile, sender=User)

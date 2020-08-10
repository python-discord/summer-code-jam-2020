import math

from PIL import Image

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.urls import reverse


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("You must have an email address")
        if not username:
            raise ValueError("You must have a username")

        user = self.model(email=self.normalize_email(email), username=username,)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email), password=password, username=username,
        )
        user.is_admin = True
        user.is_superuser = True
        user.points = 1000
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """
    Every user has:
    -username,
    -email,
    -password,

    Along with:
    -Posts,
    -Comments,
    -Likes,

    """

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(blank=False, max_length=30)

    points = models.IntegerField(default=0)

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"  # Cannot be included in required fields
    REQUIRED_FIELDS = ["email", "password"]

    objects = AccountManager()

    def __str__(self):
        return self.email

    @property
    def number_of_posts(self):
        return self.posts.count()

    @property
    def number_of_likes(self):
        return self.blog_posts_likes.count()

    @property
    def number_of_comments(self):
        return self.comments.count()

    @property
    def number_of_messages(self):
        return self.messages.count()

    @property
    def number_of_searches(self):
        return self.searches.count()

    @property
    def side_statistics(self):
        side_stats = {
            "posts": self.number_of_posts,
            "comments": self.number_of_comments,
            "likes": self.number_of_likes,
            "messages": self.number_of_messages,
            "searches": self.number_of_searches,
        }

        for name, val in side_stats.items():
            yield name.capitalize(), val

    @property
    def score(self):
        posts_weight = 13
        comments_weight = 7
        likes_weight = 3
        searches_weight = 5
        messages_weight = 1
        points_weight = 13

        rv_dict = {
            self.number_of_posts: posts_weight,
            self.number_of_comments: comments_weight,
            self.number_of_likes: likes_weight,
            self.number_of_searches: searches_weight,
            self.number_of_messages: messages_weight,
            self.points: points_weight,
        }
        rv = sum([k * v for k, v in rv_dict.items()]) // 1

        return int(rv)

    @property
    def level(self):
        level = int(math.log(self.score + 1, 1.4) // 3)
        return level

    @property
    def app_links_gen(self):
        yield "Default Search Engine", reverse("engine-results", args=["CERN"])

        if self.blogs_unlocked:
            yield "Blog", reverse("blogs_list")

        if self.weather_unlocked:
            yield "Weather", reverse("weather_results", args=["australia"])

        if self.messenger_unlocked:
            link = reverse("chat-room", kwargs={"room_name": "lobby"})
            yield "Messenger", link

    @property
    def unlocked_list_gen(self):
        yield "The early internet"
        if self.avatar_display_unlocked:
            yield "Avatar dashboard display"
        if self.blogs_unlocked:
            yield "Blogs app"
        if self.profile_change_unlocked:
            yield "Ability to change profile"
        if self.weather_unlocked:
            yield "Weather app"
        if self.like_unlocked:
            yield "Ability to like blog posts"
        if self.comments_unlocked:
            yield "Ability to comment on blog posts"
        if self.bio_unlocked:
            yield "Ability to change biography"
        if self.messenger_unlocked:
            yield "Messenger app"

    @property
    def avatar_display_unlocked(self):
        return True if self.level >= 1 else False

    @property
    def blogs_unlocked(self):
        return True if self.level >= 2 else False

    @property
    def profile_change_unlocked(self):
        return True if self.level >= 3 else False

    @property
    def blogs_posting_unlocked(self):
        return True if self.level >= 3 else False

    @property
    def weather_unlocked(self):
        return True if self.level >= 4 else False

    @property
    def like_unlocked(self):
        return True if self.level >= 5 else False

    @property
    def comments_unlocked(self):
        return True if self.level >= 6 else False

    @property
    def bio_unlocked(self):
        return True if self.level >= 7 else False

    @property
    def messenger_unlocked(self):
        return True if self.level >= 8 else False

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="profile"
    )
    biography = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(
        default="default.png", upload_to="avatars/", max_length=300
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

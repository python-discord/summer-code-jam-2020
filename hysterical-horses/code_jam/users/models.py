from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('You must have an email address')
        if not username:
            raise ValueError('You must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_superuser = True
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
    searches_made = models.IntegerField(default=0)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # Cannot be included in required fields
    REQUIRED_FIELDS = ['email', 'password']

    objects = AccountManager()

    def __str__(self):
        return self.email

    @property
    def number_of_posts(self):
        return len(self.posts.all())

    @property
    def number_of_likes(self):
        return len(self.all_likes.all())

    @property
    def number_of_comments(self):
        return  # No idea what to return here

    @property
    def number_of_messages(self):
        return  # No idea as well

    @property
    def score(self):
        return self.number_of_likes + self.number_of_posts

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user.username} Profile"

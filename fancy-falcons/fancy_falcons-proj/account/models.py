from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from PIL import Image


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, earldom, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not earldom:
            raise ValueError("User must have an earldom")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            earldom=earldom,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, earldom, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            earldom=earldom,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email =         models.EmailField(verbose_name='email', max_length=60, unique=True)
    title =         models.CharField(max_length=20, default='Earl', editable=False)
    first_name =    models.CharField(max_length=30)
    last_name =     models.CharField(max_length=100)
    earldom =       models.CharField(max_length=50)
    short_bio =     models.CharField(max_length=300, blank=True)
    image =         models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday =      models.DateField(blank=True, null=True)
    is_user =       models.BooleanField(default=True)
    is_admin =      models.BooleanField(default=False)
    is_active =     models.BooleanField(default=True)
    is_staff =      models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'earldom',
    ]

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.title} {self.first_name} {self.last_name} of {self.earldom}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def save(self, *args, **kwargs):
        super(Account, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def has_module_perms(self, app_label):
        return True

    @property
    def get_html_url(self):
        url = reverse('earls:earldetail', args=(self.id,))
        return f'<a href="{url}"> Earl {self.first_name} {self.last_name} </a>'

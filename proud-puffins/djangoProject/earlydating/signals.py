from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Profile


#  Listen to Users table and crete a new profile whenever new user is created
def create_profile(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        try:
            group = Group.objects.get(name='profile')
        except Group.DoesNotExist:
            group = Group.objects.create(name='profile')
        instance.groups.add(group)
        Profile.objects.create(user=instance)


#  register post_save signal
post_save.connect(create_profile, sender=User)

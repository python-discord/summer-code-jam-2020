from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    """Listen to Users table and create a new profile whenever a user is created"""
    # If the user is created and not by loading a fixture
    if created and not kwargs.get('raw', False):
        try:
            group = Group.objects.get(name='profile')
        except Group.DoesNotExist:
            group = Group.objects.create(name='profile')
        # Add user to profile group and create profile object
        instance.groups.add(group)
        Profile.objects.create(user=instance)


#  register post_save signal
post_save.connect(create_profile, sender=User)

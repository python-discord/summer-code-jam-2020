from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()

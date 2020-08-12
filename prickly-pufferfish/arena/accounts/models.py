from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from battle.models import Battle


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def battles_won(self):
        self.user.challenges.filter(victory=True).count()

    def in_battle(self):
        return self.user.battles.filter(state=Battle.ACTIVE).count() > 0

    def current_battle(self):
        if self.in_battle():
            return self.user.battles.get(state=Battle.ACTIVE)
        else:
            return None

    def __str__(self):
        return f'Profile for user {self.user.username}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

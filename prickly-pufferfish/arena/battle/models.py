from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Battle(models.Model):
    WAITING = 'W'
    READY = 'E'
    ACTIVE = 'A'
    ARCHIVED = 'R'
    STATES = [
        (WAITING, 'Waiting for Players'),
        (READY, 'Ready to Start'),
        (ACTIVE, 'Battle in Progress'),
        (ARCHIVED, 'Battle Over'),
    ]

    time_created = models.DateTimeField(auto_now_add=True)
    challengers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='Challenger', related_name='battles'
    )
    state = models.CharField(choices=STATES, max_length=1, default=WAITING)

    def clean(self):
        if self.challengers.count() >= 2:
            raise ValidationError('There can only be up to 2 challengers in a battle!')

    def __str__(self):
        state = dict(self.STATES)[self.state]
        return f'Battle ID: {self.pk}, Timestamp: {self.time_created}, {state}'


class Challenger(models.Model):
    RED = 'R'
    BLUE = 'B'

    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='challenges'
    )
    color = models.CharField(
        choices=[(RED, 'Red'), (BLUE, 'Blue')], max_length=1, default=RED
    )
    victory = models.BooleanField(default=False)

    def __str__(self):
        color = 'Red' if self.color == 'R' else 'Blue'
        return f'{color} challenger {self.user.username} to battle {self.battle.pk}'

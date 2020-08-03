from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class VMachine(models.Model):
    name = models.CharField(max_length=20)
    shell_choices = [
        ('sh', 'Sh'),
        ('bash', 'Bash'),
        ('zsh', 'Zsh'),
    ]
    shells = models.CharField(
        max_length=4,
        choices=shell_choices,
    )
    floppy_disks_id = ArrayField(models.CharField(max_length=10))
    floppy_disks_name = ArrayField(models.CharField(max_length=10))
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Floppy(models.Model):
    name = models.CharField(max_length=10)
    storage_id = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

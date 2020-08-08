from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class VMachine(models.Model):
    name = models.CharField(max_length=20)
    shell_choices = [
        ('sh', 'Sh'),
        ('bash', 'Bash'),
        ('zsh', 'Zsh'),
        ('dash', 'Dash')
    ]
    shells = models.CharField(
        max_length=4,
        choices=shell_choices,
    )
    floppy_disks_id = ArrayField(models.CharField(max_length=30, null=True), null=True, default=list)
    floppy_disks_name = ArrayField(models.CharField(max_length=300, null=True), null=True, default=list)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}({self.pk})'


class Floppy(models.Model):
    name = models.CharField(max_length=300)
    storage_id = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vm = models.ForeignKey(VMachine, on_delete=models.CASCADE, default=None)

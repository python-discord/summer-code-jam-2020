from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    title = models.CharField(max_length=255, blank=True)
    hash_val = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title} hash_val :{self.hash_val} uploaded_at {self.uploaded_at}"


class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through='Member')

    def __str__(self):
        return f"{self.name} created on {self.created_at}\nMember(s): {self.members.all()}"


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"User: {self.user} belongs to {self.team}"

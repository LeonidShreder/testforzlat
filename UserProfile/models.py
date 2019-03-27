from django.db import models
from django.contrib.auth.models import AbstractUser


class Friend(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class User(AbstractUser):
    age = models.IntegerField(blank=True, default=1)
    friend = models.ManyToManyField(Friend)

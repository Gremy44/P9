from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Subscription(models.Model):
    follower = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE,
        related_name='subscriptions')
    followed = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE,
        related_name='friends')

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = models.CharField(max_length=40,verbose_name="Nom d'utilisateur")
    # firstname = models.CharField(max_length=40)
    # lastname = models.CharField(max_length=40)
    # birthday = models.DateField(blank=True)
    # profile_photo = models.ImageField()
    # email = models.EmailField(max_length=50, null=True)
    pass

class Subscription(models.Model):
    follower = models.ForeignKey(User, null = True, on_delete=models.CASCADE, related_name='subscriptions')
    followed = models.ForeignKey(User, null = True, on_delete=models.CASCADE, related_name='friends')

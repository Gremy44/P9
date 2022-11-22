from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = models.CharField(max_length=40)
    # firstname = models.CharField(max_length=40)
    # lastname = models.CharField(max_length=40)
    # birthday = models.DateField(blank=True)
    # profile_photo = models.ImageField()
    # email = models.EmailField(max_length=50, null=True)
    pass



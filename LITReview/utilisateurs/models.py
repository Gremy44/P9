from django.db import models

class Users(models.Model):
    first_name = models.fields.CharField(max_length = 100)
    last_name = models.fields.CharField(max_length = 100)
    user_name = models.fields.CharField(max_length = 100)
    birthday = models.fields.DateField()

class Subscription(models.Model):
    pass

# Create your models here.

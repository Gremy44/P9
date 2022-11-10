from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    user_name = models.fields.CharField(max_length = 100)
    first_name = models.fields.CharField(max_length = 100)
    last_name = models.fields.CharField(max_length = 100)
    birthday = models.fields.DateField()
    
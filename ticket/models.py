from django.db import models
from django.conf import settings
from PIL import Image

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE, Image.ANTIALIAS)
        image.save(self.image.path, "JPEG")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=5000)
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    adult = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)

class Critique(models.Model):
    RATE_1 = 1
    RATE_2 = 2
    RATE_3 = 3
    RATE_4 = 4
    RATE_5 = 5

    RATE_CHOICES = [
                    (RATE_1, '1 étoile'),
                    (RATE_2, '2 étoiles'),
                    (RATE_3, '3 étoiles'),
                    (RATE_4, '4 étoiles'),
                    (RATE_5, '5 étoiles'),
                   ]

    title = models.CharField(max_length=128)
    rate = models.CharField(
           max_length=1,
           choices=RATE_CHOICES,
           default=RATE_1,
    )
    comment = models.TextField(max_length=5000)

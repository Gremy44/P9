from django.db import models
from django.conf import settings
from PIL import Image

RATE_CHOICES = [
                    ('1', '1 étoile'),
                    ('2', '2 étoiles'),
                    ('3', '3 étoiles'),
                    ('4', '4 étoiles'),
                    ('5', '5 étoiles'),
                   ]

class Photo(models.Model):
    image = models.ImageField()
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
    title = models.CharField(max_length=128, verbose_name='Titre du livre')
    content = models.TextField(max_length=5000, verbose_name='Description')
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    

class Critique(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, verbose_name='Titre de la critique')
    rate = models.CharField(
           max_length=1,
           choices=RATE_CHOICES,
           default='1',
    )
    comment = models.TextField(max_length=5000, verbose_name='Votre commentaire')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    
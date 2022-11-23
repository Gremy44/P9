from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket import models

@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'news_feed/home.html', context={'photos': photos})

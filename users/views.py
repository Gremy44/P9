from django.shortcuts import render
from django.http import HttpResponse
from users.models import User

def login(request):
    users = User.objects.all()
    return render(request, 'users/login.html', context={"users":users})

def registration(request):
    return HttpResponse('<h1>registration view</h1>')

def subscription(request):
    return HttpResponse('<h1>subscription view</h1>')

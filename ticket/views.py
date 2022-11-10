from django.shortcuts import render
from django.http import HttpResponse

def review(request):
    HttpResponse('<h1>c_review view</h1>')

def ticket(request):
    HttpResponse('<h1>c_ticket view</h1>')

def ticket_review(request):
    HttpResponse('<h1>c_ticket_review view</h1>')
# Create your views here.

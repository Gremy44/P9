from django.contrib import admin
from django.urls import path
from ticket import views

urlpatterns = [
    path('review/', views.review),
    path('ticket/', views.ticket),
    path('ticket_review/', views.ticket_review)
]
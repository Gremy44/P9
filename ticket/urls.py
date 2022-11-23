from django.urls import path

from ticket import views

urlpatterns = [
    path('ticket/upload/', views.photo_upload, name='ticket_upload'),
]
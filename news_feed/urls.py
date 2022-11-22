from django.urls import path

import news_feed.views

urlpatterns = [
    path('home/', news_feed.views.home, name='home'),
]
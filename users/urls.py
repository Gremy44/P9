from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html',
         redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('registration/', views.registration_page, name='registration'),
    path('subscription/', views.subscription, name='subscription'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]

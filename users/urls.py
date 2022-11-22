from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

import users.views

urlpatterns = [
    path('login/', LoginView.as_view(
            template_name='users/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(
            template_name='users/logout.html'
            ),
        name='logout'),
    # path('login/', users.views.LoginPageView.as_view(), name='login'),
    # path('logout/', users.views.logout_user, name='logout'),
    #path('registration/', views.registration),
    #path('subscription/', views.subscription),
]
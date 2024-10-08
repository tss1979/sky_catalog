from django.contrib.auth.views import LoginView, LogoutView
from django.template.defaulttags import url
from django.urls import path

from config import settings
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, recover_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('recover_password/', recover_password, name='recover_password'),
]
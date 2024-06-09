from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserSignup, UserView

urlpatterns = [
    path("register", UserSignup.as_view()),
    path("me", UserView.as_view()),
    path("login", obtain_auth_token, name="login_api_view"),
]

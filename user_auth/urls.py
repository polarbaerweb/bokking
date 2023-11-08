from django.urls import path

from .views import user_login, user_logout, user_signup

app_name = "user_auth"

urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", user_signup, name="signup"),
    path("logout/", user_logout, name="logout"),
]

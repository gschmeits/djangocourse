from django.urls import path
from . import views

#app_name = "account"

urlpatterns = [
    path("", views.home, name=""),
    path("register/", views.register, name="register"),
    path("my_login/", views.user_login, name="my-login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]

from django.urls import path, include
from . import urls_reset
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("password-reset/", include(urls_reset)),
]

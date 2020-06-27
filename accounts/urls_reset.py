from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

"""
This password reset URL is an upgrade of CI code from Django=1.11 to Django=3.

The registration folder with the password reset templates are stored in the main template folder.
"""
urlpatterns = [
    path('', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

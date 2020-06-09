from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as AuthViews

"""
This password reset URL is an upgrade of CI code from Django=1.11 to Django=3.

The registration folder with the password reset templates are stored in the main template folder.
"""
urlpatterns = [
    path('', AuthViews.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('done/', AuthViews.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', AuthViews.PasswordResetConfirmView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_confirm'),
    path('complete/', AuthViews.PasswordResetConfirmView.as_view(), name='password_reset_complete')
]

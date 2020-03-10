from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as AuthViews

urlpatterns = [
    path('', AuthViews.PasswordResetView.as_view(template_name='registration/password_reset_done.html'), name='password_reset'),
    path('done/', AuthViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', AuthViews.PasswordResetConfirmView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_confirm'),
    path('complete/', AuthViews.PasswordResetConfirmView.as_view(), name='password_reset_complete')
]

from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as AuthViews

urlpatterns = [
    path('', AuthViews.PasswordReset.as_view({'post_reset_redirect': reverse_lazy('password_reset_done')}), name='password_reset'),
    path('done/', AuthViews.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', AuthViews.password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('complete/', AuthViews.password_reset_complete, name='password_reset_complete')
]

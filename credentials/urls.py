from django.urls import path
from .views import BlogRegisterView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', BlogRegisterView.as_view(), name='register'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset.html')),
    path('password/', PasswordsChangeView.as_view(template_name='password_reset.html')),
    path('password_success', views.password_success, name="password_success.html")
]

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('post_list/', views.post_list, name='post_list'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("webauthn/", include("django_otp_webauthn.urls", namespace="otp_webauthn")),
    # other paths...
]
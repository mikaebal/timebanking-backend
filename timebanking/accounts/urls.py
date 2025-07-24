from django.urls import path
from .views import profile_view, register_view, login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name="login"),
    path('profile/', profile_view, name='profile'),
]
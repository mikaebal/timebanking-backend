from django.urls import path
from .views import profile_view, register_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', obtain_auth_token),
    path('profile/', profile_view, name='profile'),
]
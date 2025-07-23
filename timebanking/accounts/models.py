from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)      # ensure unique email
    bio = models.TextField(blank=True)      # allow empty bio
    avatar = models.URLField(blank=True)      # allow empty avatar (later use cloudinary)
    credits = models.IntegerField(default=0)      # credits start at 0
    created_at = models.DateTimeField(auto_now_add=True)      # auto record when user is created

    # set login field to email instead of default username
    USERNAME_FIELD = 'email'
    # required username for creating superuser
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email  # shows email in admin
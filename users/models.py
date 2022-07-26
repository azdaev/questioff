from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

User._meta.get_field('email').blank = False


class CustomUser(AbstractUser):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

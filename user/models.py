from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.TextField(max_length=10, blank=True)
    address = models.TextField(max_length=100, blank=True)
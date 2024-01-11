from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from cbrf.settings import ROLES


class CustomUser(AbstractUser):
    role = models.CharField(max_length=9, choices=ROLES, default="User")

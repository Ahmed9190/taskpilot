from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = "user"
    EMPLOYER = "employer"
    ADMIN = "admin"

    ROLE_CHOICES = [
        (USER, "User"),
        (EMPLOYER, "Employer"),
        (ADMIN, "Admin"),
    ]

    role: models.CharField = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default=USER
    )

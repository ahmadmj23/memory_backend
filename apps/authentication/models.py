from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        NORMAL_USER = 'normal_user', 'Normal User'
        REVIEWER = 'reviewer', 'Reviewer'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.NORMAL_USER,
        help_text="User role for permission handling"
    )
    
    is_verified = models.BooleanField(
        default=False,
        help_text="Designates whether this user has verified their email via OTP."
    )
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

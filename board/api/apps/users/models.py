from django.contrib.auth.models import AbstractUser

from apps.core.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    """User"""

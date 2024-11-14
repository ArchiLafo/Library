from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):

    phone = models.CharField(
        max_length=13,
        blank=True,
        null=True,
    )

    def __set__(self):
        return self.username

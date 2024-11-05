from django.db import models
from django.contrib.auth.models import AbstractUser 


class CustomUser(AbstractUser):

    date_of_birth = models.DateField(verbose_name="date of birth")
    can_be_contacted = models.BooleanField(
        default=False,
        verbose_name="contact consent"
        )
    can_data_be_shared = models.BooleanField(
        default=False,
        verbose_name="data share consent"
        )

    def __str__(self):
        return self.username

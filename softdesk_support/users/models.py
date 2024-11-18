from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's default AbstractUser.

    Attributes:
        date_of_birth (DateField): The user's date of birth.
        can_be_contacted (BooleanField): Indicates if the user has consented
            to being contacted.
        can_data_be_shared (BooleanField): Indicates if the user has consented
            to data sharing.
    """

    date_of_birth = models.DateField(verbose_name="date of birth")
    can_be_contacted = models.BooleanField(
        default=False,
        verbose_name="contact consent"
        )
    can_data_be_shared = models.BooleanField(
        default=False,
        verbose_name="data share consent"
        )

    def clean(self):
        """Check if user have the minimum age required."""
        MINIMUM_AGE = 15
        super().clean()
        if self.date_of_birth:
            today = now().date()
            min_age_date = today.replace(year=today.year - MINIMUM_AGE)
            if self.date_of_birth > min_age_date:
                raise ValidationError(
                    f"You must be at least {MINIMUM_AGE} years old to register."
                )
        
    def __str__(self):
        """Return the string representation of the user."""
        return self.username

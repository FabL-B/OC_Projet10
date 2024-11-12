from django.db import models
from users.models import CustomUser
from projects.models import Project


class Contributor(models.Model):
    """Class that defines a contributor."""

    ROLE = [
        ("Owner", "Owner"),
        ("Contributor", "Contributor"),
    ]

    user = models.ForeignKey(CustomUser,
                            on_delete=models.CASCADE,
                            related_name="contributions"
                            )
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="contributors"
                                )
    role = models.CharField(max_length=20, choices=ROLE, default="Contributor")
    
    def __str__(self):
        return f"{self.user.username} - {self.project.name}"

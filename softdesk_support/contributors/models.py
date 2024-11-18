from django.db import models
from users.models import CustomUser
from projects.models import Project


class Contributor(models.Model):
    """
    Model that defines a contributor to a project.

    Attributes:
        user (ForeignKey): The user who contributes to the project.
        project (ForeignKey): The project the user is contributing to.
        role (CharField): The role of the contributor within the project.
    """

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
        """Return a string representation of the contributor."""
        return f"{self.user.username} - {self.project.name}"

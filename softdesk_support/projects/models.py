from django.db import models
from users.models import CustomUser


class Project(models.Model):
    """
    Model that defines a project.

    Attributes:
        author (ForeignKey): The user who created the project.
        type (CharField): The type of the project.
        created_time (DateTimeField): The timestamp when the project was created.
        name (CharField): The name of the project.
        description (TextField): A detailed description of the project.
    """

    PROJECT_TYPES = [
        ("Backend", "Backend"),
        ("Frontend", "Frontend"),
        ("iOS", "iOS"),
        ("Android", "Android"),
    ]

    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name="projects"
                               )
    type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    created_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """Return the name of the project."""
        return self.name

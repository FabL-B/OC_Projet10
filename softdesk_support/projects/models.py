from django.db import models
from users.models import CustomUser


class Project(models.Model):
    """Class that defines a projet."""

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
        return self.name

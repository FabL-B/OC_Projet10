from django.db import models

from users.models import CustomUser
from projects.models import Project
from contributors.models import Contributor


class Issue(models.Model):
    """
    Model that defines an issue within a project.

    Attributes:
        author (ForeignKey): The user who created the issue.
        project (ForeignKey): The project the issue belongs to.
        title (CharField): The title of the issue.
        description (TextField): A detailed description of the issue.
        assigned_to (ForeignKey): The contributor assigned to handle the issue.
        priority (CharField): The priority level of the issue.
        tag (CharField): The type of issue.
        status (CharField): The current status of the issue.
        created_time (DateTimeField): The timestamp when the issue was created.
    """

    PRIORITIES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]
    TAGS = [
        ("Bug", "Bug"),
        ("Feature", "Feature"),
        ("Task", "Task"),
    ]
    STATUS_CHOICES = [
        ("To_do", "To do"),
        ("In_progress", "In progress"),
        ("Finished", "Finished"),
    ]

    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name="issue_author"
                               )
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="issues"
                                )
    title = models.CharField(max_length=255,)
    description = models.TextField(max_length=2000)
    assigned_to = models.ForeignKey(Contributor,
                                    on_delete=models.CASCADE,
                                    related_name="assigned_issues"
                                    )
    priority = models.CharField(max_length=20, choices=PRIORITIES, default="Low")
    tag = models.CharField(max_length=20, choices=TAGS, default="Bug")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To_do")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the issue."""
        return f"Issue: {self.title} - Project: {self.project.name}"

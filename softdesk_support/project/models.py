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


class Issue(models.Model):
    """Class that defines an issue."""
    
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


class Comments(models.Model):
    
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name="comments"
                               )
    issue = models.ForeignKey(Issue,
                              on_delete=models.CASCADE,
                              related_name="comments"
                              )
    description = models.TextField(max_length=2000)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.issue}"

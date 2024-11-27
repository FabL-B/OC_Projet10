import uuid
from django.db import models

from users.models import CustomUser
from issues.models import Issue


class Comment(models.Model):
    """
    A class representing a comment made by a user on an issue.

    Attributes:
        id (UUIDField): A unique identifier for the comment
        author (ForeignKey): The user who created the comment.
        issue (ForeignKey): The issue the comment is associated with.
        description (TextField): The content of the comment
        created_time (DateTimeField): The timestamp when the comment was created.
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
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
        """Returns a string representation of the comment."""
        return f"Comment by {self.author} on {self.issue}"

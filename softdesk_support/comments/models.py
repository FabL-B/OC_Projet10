import uuid
from django.db import models

from users.models import CustomUser
from issues.models import Issue


class Comment(models.Model):
    """A class that defines a comment."""
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
        return f"Comment by {self.author} on {self.issue}"

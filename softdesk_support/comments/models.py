from django.db import models
from users.models import CustomUser
from issues.models import Issue


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

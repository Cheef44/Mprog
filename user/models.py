from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Post

class UserComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.comment
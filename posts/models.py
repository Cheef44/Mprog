from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_image = models.ImageField(upload_to=settings.MEDIA_ROOT + 'users/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=200)
    main_text = models.TextField()
    text = models.TextField()
    file = models.FileField(upload_to=settings.MEDIA_ROOT + 'users/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT + 'users/%Y/%m/%d/', blank=True)
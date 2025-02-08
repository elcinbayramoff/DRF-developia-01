from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model): 
    title = models.CharField(max_length=150)
    content = models.TextField()
    comment_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    like_count = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)
    

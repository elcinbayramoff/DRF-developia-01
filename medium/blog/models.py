from django.db import models

# Create your models here.
class Article(models.Model): #id = 1
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE) # 1
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
"""
{
    "article":1,
    "content":"Salam"
}

"""
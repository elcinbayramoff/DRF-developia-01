from django.contrib import admin
from .models import Article, Comment

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','creator']
    list_editable = ['creator']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','article', 'content']
    

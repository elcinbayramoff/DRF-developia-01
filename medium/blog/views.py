from django.shortcuts import render
from rest_framework import status

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.validators import ValidationError

"""
GET - > All Articles +
POST - > Create new article +
GET (RETRIVE) -> Sadəcə 1 Article
PUT -> Datanı dəyişir
PATCH -> Datanı qismən dəyişir
DELETE -> Datanı silir
"""



@api_view(['GET', 'POST']) 
def index(request):
    """
    Bütün articleları qaytarmaq GET
    Article yaratmaq POST
    """
    
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) # serializing
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data) #Create
        is_valid = serializer.is_valid() # True, False
        
        if is_valid:
            data = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# @api_view(['POST'])
# def create_article(request):
    
#     serializer = ArticleSerializer(data=request.data) #Create
#     is_valid = serializer.is_valid() # True, False
    
#     if is_valid:
#         data = serializer.save()
#         return Response({'detail':serializer.data})
#     else:
#         return Response(serializer.errors)

"""
PUT -> Update
PATCH -> Partially Update
"""
@api_view(['GET','PUT','PATCH','DELETE'])
def article_actions(request, pk):
    
    if request.method == 'PATCH':
        try:
            article = Article.objects.get(id=pk)
            
        except Article.DoesNotExist:
            raise ValidationError({'detail':'This article does not exist'})
        
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        is_valid = serializer.is_valid()
        
        if is_valid:
            data = serializer.save()
            return Response({'detail':serializer.data})
        else:
            return Response(serializer.errors)
        
    elif request.method == 'PUT':
        try:
            article = Article.objects.get(id=pk)
            
        except Article.DoesNotExist:
            raise ValidationError({'detail':'This article does not exist'})
        
        serializer = ArticleSerializer(instance=article, data=request.data)
        is_valid = serializer.is_valid()
        
        if is_valid:
            data = serializer.save()
            return Response({'detail':serializer.data})
        else:
            return Response(serializer.errors)
        
    elif request.method == 'GET':
        
        try:
            article = Article.objects.get(id=pk)
            
        except Article.DoesNotExist:
            raise ValidationError({'detail':'This article does not exist'})
            
        serializer = ArticleSerializer(article)
        
        return Response(serializer.data)
    
    elif request.method == 'DELETE':

        try:
            article = Article.objects.get(id=pk)
            
        except Article.DoesNotExist:
            raise ValidationError({'detail':'This article does not exist'})
        
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
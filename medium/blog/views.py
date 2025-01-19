from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    # article = articles.first()
    
    serializer = ArticleSerializer(articles, many=True) # serializing
    return Response(serializer.data)

@api_view(['GET'])
def create_article(request):
    
    data1 = {
            'title':'Article 3',
            'content':'Content of Article 3'
        }
    
    serializer = ArticleSerializer(data=data1) #Create
    is_valid = serializer.is_valid() # True, False
    
    if is_valid:
        data = serializer.save()
        return Response({'detail':serializer.data})
    else:
        return Response(serializer.errors)
    
    
@api_view(['GET'])
def update_article(request):
    
    data1 = {
            'title':'Article 125332489329847923',
            'content':'Content of Article 125'
        }
    
    article = Article.objects.get(id=4)
    
    serializer = ArticleSerializer(instance=article, data=data1)
    is_valid = serializer.is_valid() # True, False
    
    if is_valid:
        data = serializer.save()
        return Response({'detail':serializer.data})
    else:
        return Response(serializer.errors)
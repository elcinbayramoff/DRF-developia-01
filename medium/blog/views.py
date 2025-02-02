from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.validators import ValidationError
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action

#CRUD - Create, Read, Update, Delete

class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        comment = self.get_object() #comments/7/like/ -> pk = 7 -> Comment.objects.get(id=7)
        comment.like_count += 1
        comment.save()
        
        return Response({'detail':'Comment liked successfully'}, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['GET'])
    def popular(self, request):
        #like_count'u 7 ve 7den yuxarı olanlar >= 7 greater than equal gte
        #gte - >=
        #gt - >
        #lt - <
        #lte - <=
        #exact - ==
        #in - in 
        #range - range
        #isnull - ==None
        
        comments = Comment.objects.filter(like_count__range=(3,7))
        serializer = self.get_serializer(comments, many=True)
        
        return Response(serializer.data)
    
    
    
    
    
"""
GET - > All Articles +
POST - > Create new article +
GET (RETRIVE) -> Sadəcə 1 Article
PUT -> Datanı dəyişir
PATCH -> Datanı qismən dəyişir
DELETE -> Datanı silir
"""


"""
# @api_view(['GET', 'POST']) 
# def index(request):
#     
#     Bütün articleları qaytarmaq GET
#     Article yaratmaq POST
#     
    
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True) # serializing
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data) #Create
#         is_valid = serializer.is_valid() # True, False
        
#         if is_valid:
#             data = serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# # @api_view(['POST'])
# # def create_article(request):
    
# #     serializer = ArticleSerializer(data=request.data) #Create
# #     is_valid = serializer.is_valid() # True, False
    
# #     if is_valid:
# #         data = serializer.save()
# #         return Response({'detail':serializer.data})
# #     else:
# #         return Response(serializer.errors)

# 
# PUT -> Update
# PATCH -> Partially Update
# 
# @api_view(['GET','PUT','PATCH','DELETE'])
# def article_actions(request, pk):
    
#     if request.method == 'PATCH':
#         try:
#             article = Article.objects.get(id=pk)
            
#         except Article.DoesNotExist:
#             raise ValidationError({'detail':'This article does not exist'})
        
#         serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
#         is_valid = serializer.is_valid()
        
#         if is_valid:
#             data = serializer.save()
#             return Response({'detail':serializer.data})
#         else:
#             return Response(serializer.errors)
        
#     elif request.method == 'PUT':
#         try:
#             article = Article.objects.get(id=pk)
            
#         except Article.DoesNotExist:
#             raise ValidationError({'detail':'This article does not exist'})
        
#         serializer = ArticleSerializer(instance=article, data=request.data)
#         is_valid = serializer.is_valid()
        
#         if is_valid:
#             data = serializer.save()
#             return Response({'detail':serializer.data})
#         else:
#             return Response(serializer.errors)
        
#     elif request.method == 'GET':
        
#         try:
#             article = Article.objects.get(id=pk)
            
#         except Article.DoesNotExist:
#             raise ValidationError({'detail':'This article does not exist'})
            
#         serializer = ArticleSerializer(article)
        
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':

#         try:
#             article = Article.objects.get(id=pk)
            
#         except Article.DoesNotExist:
#             raise ValidationError({'detail':'This article does not exist'})
        
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
# python manage.py makemigrations
# python manage.py migrate
        
@api_view(['GET', 'POST']) 
def index_comment(request):

    Bütün Commentleri qaytarmaq GET
    Comment yaratmaq POST
    
    
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True) # serializing
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data) #Create
        is_valid = serializer.is_valid() # True, False
        
        if is_valid:
            data = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        
@api_view(['GET','PUT','PATCH','DELETE'])
def comment_actions(request, pk):
    
    if request.method == 'PATCH':
        try:
            comment = Comment.objects.get(id=pk)
            
        except Comment.DoesNotExist:
            raise ValidationError({'detail':'This comment does not exist'})
        
        serializer = CommentSerializer(instance=comment, data=request.data, partial=True)
        is_valid = serializer.is_valid()
        
        if is_valid:
            data = serializer.save()
            return Response({'detail':serializer.data})
        else:
            return Response(serializer.errors)
        
        
    elif request.method == 'PUT':
        try:
            comment = Comment.objects.get(id=pk)
            
        except Comment.DoesNotExist:
            raise ValidationError({'detail':'This comment does not exist'})
        
        serializer = CommentSerializer(instance=comment, data=request.data)
        
        if serializer.is_valid():
            data = serializer.save()
            return Response({'detail':serializer.data})
        else:
            return Response(serializer.errors)
        
    elif request.method == 'GET':
        
        try:
            comment = Comment.objects.get(id=pk)
            
        except Comment.DoesNotExist:
            raise ValidationError({'detail':'This comment does not exist'})
            
        serializer = CommentSerializer(comment)
        
        return Response(serializer.data)
    
    elif request.method == 'DELETE':

        try:
            comment = Comment.objects.get(id=pk)
            
        except Comment.DoesNotExist:
            raise ValidationError({'detail':'This comment does not exist'})
        
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

"""
"""
# class ArticleAPIView(APIView):
#     def get(self, request, pk=None):

#         if pk:
#             try:
#                 article = Article.objects.get(id=pk)
                
#             except Article.DoesNotExist:
#                 raise ValidationError({'detail':'This article does not exist'})
                
#             serializer = ArticleSerializer(article)
            
#             return Response(serializer.data)
        
#         else:
#             articles = Article.objects.all()
#             serializer = ArticleSerializer(articles, many=True) # serializing
#             return Response(serializer.data)
        
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data) #Create
        
#         if serializer.is_valid():
#             data = serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def put(self, request, pk):
#         try:
#             article = Article.objects.get(id=pk)
            
#         except Article.DoesNotExist:
#             raise ValidationError({'detail':'This article does not exist'})
        
#         serializer = ArticleSerializer(instance=article, data=request.data)
#         is_valid = serializer.is_valid()
        
#         if is_valid:
#             data = serializer.save()
#             return Response({'detail':serializer.data})
#         else:
#             return Response(serializer.errors)
        
#     def patch(self, request, pk):
#         try:
#             article = Article.objects.get(id=pk)
            
#         except Article.DoesNotExist:
#             raise ValidationError({'detail':'This article does not exist'})
        
#         serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
#         is_valid = serializer.is_valid()
        
#         if is_valid:
#             data = serializer.save()
#             return Response({'detail':serializer.data})
#         else:
#             return Response(serializer.errors)
        
#     def delete(self, request, pk):
#         try:
#             article = Article.objects.get(id=pk)
            
#         except Article.DoesNotExist:
#             raise ValidationError({'detail':'This article does not exist'})
        
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
get - list, retrieve
post - create
put - update
patch - update
delete - destroy
"""

# class ArticleDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    
# class ArticleGenericAPIView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    

# class CommentDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
# class CommentGenericAPIView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
    

#CommentSerializer
#Comment

#mixins, generics, viewsets

    

    
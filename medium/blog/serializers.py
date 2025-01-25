from rest_framework import serializers
from .models import Article, Comment
from rest_framework.serializers import ValidationError
"""
Back >JSON >FRONT

Dictionary vs JSON
Serializing 
model -> json
Deserializing
json -> model
"""


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ['id','title','content','created_at']
        
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
    
#     #Validating fields, General Validating
#     def validate_title(self, data):
#         print(data)
#         print(len(data))
#         if len(data) < 20:
#             raise ValidationError('20den boyuk olmalidir')
        
#         return data

#     def validate(self, data):
        
#         if 'Azerbaycan' not in data['title'] and 'Azerbaycan' not in data['content']:
#             raise ValidationError('Azerbaycan olmalidir')

        
#         return data    

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
    
#     #Full update, partial update
#     def update(self, instance, validated_data):
        
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
        
#         return instance
    
#     # def save(self):
#     #     print('title')
#     #     print('content')
        
        
    
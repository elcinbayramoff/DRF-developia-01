from django.urls import path
from .views import ArticleAPIView, index_comment, comment_actions

urlpatterns = [
    path('', ArticleAPIView.as_view()),
    # path('create_article',create_article),
    path('article/<int:pk>/',ArticleAPIView.as_view()),
    
    path('comment/', index_comment),
    # path('create_article',create_article),
    path('comment/<int:pk>/',comment_actions),

]
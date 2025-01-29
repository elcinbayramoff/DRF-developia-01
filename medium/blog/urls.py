from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import index_comment, comment_actions, ArticleGenericAPIView, ArticleDetailGenericAPIView

router = DefaultRouter()
# router.register(r'articles', ArticleGenericAPIView, basename='articles')

urlpatterns = [
    # path('', ArticleAPIView.as_view()),
    # # path('create_article',create_article),
    # path('article/<int:pk>/',ArticleAPIView.as_view()),
    
    path('comment/', index_comment),
    # path('create_article',create_article),
    path('comment/<int:pk>/',comment_actions),
    path('articles/', ArticleGenericAPIView.as_view()),
    path('articles/<int:pk>/',ArticleDetailGenericAPIView.as_view()),

]
# urlpatterns += router.urls
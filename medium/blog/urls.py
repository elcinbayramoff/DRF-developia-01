from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (CommentModelViewSet,
                    ArticleModelViewSet                    )

router = DefaultRouter()
router.register(r'articles', ArticleModelViewSet, basename='articles')
router.register(r'comments', CommentModelViewSet, basename='comments')

urlpatterns = [
    # path('', ArticleAPIView.as_view()),
    # # path('create_article',create_article),
    # path('article/<int:pk>/',ArticleAPIView.as_view()),
    
    # path('comment/', index_comment),
    # # path('create_article',create_article),
    # path('comment/<int:pk>/',comment_actions),
    # path('articles/', ArticleGenericAPIView.as_view()),
    # path('articles/<int:pk>/',ArticleDetailGenericAPIView.as_view()),
]
urlpatterns += router.urls
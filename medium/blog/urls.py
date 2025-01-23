from django.urls import path
from .views import index, article_actions

urlpatterns = [
    path('', index),
    # path('create_article',create_article),
    path('article/<int:pk>/',article_actions),

]
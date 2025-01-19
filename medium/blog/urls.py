from django.urls import path
from .views import index, create_article, update_article

urlpatterns = [
    path('', index ),
    path('create_article',create_article),
    path('update_article',update_article),

]
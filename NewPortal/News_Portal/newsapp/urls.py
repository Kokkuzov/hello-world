from django.contrib import admin
from django.urls import path, include
from .views import (NewsList, NewsCreateView, ArticleCreateView, NewsUpdateView, ArticleUpdateView, NewsDeleteView, ArticleDeleteView)
from . import views


urlpatterns = [
   path('', NewsList.as_view(), name='news'),
   path('<int:post_id>/', views.news_detail, name='news_detail'),
   path('search/', views.news_search, name='news_search'),
   path('create/', NewsCreateView.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

   # Статьи
   path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
from django.contrib import admin
from django.urls import path, include
from .views import (NewsCreateView, ArticleCreateView, NewsUpdateView, ArticleUpdateView, NewsDeleteView,
                    ArticleDeleteView, IndexView)
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),


    path('news/', views.news_list, name='news'),
    path('news/<int:post_id>/', views.news_detail, name='news_detail'),
    path('news/search/', views.news_search, name='news_search'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='confirm_delete'),

   # Статьи
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:post_id>/', views.news_detail, name='articles_detail'),
    path('articles/search/', views.articles_search, name='article_search'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='confirm_delete'),
]
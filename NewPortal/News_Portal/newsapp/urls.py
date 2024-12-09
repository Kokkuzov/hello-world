from django.urls import path
from .views import NewsList
from . import views


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:post_id>/', views.news_detail, name='news_detail'),
]
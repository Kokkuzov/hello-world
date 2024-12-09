from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render, get_object_or_404

class NewsList(ListView):
    model = Post
    ordering = 'text'
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


def news_list(request):
    news = Post.objects.filter(post_type='новость').order_by('-created_at')

    return render(request, 'news_list.html', {'news': news})


def news_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'news_detail.html', {'post': post})
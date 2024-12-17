from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .filters import News_filters
from .models import Post, Author
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context


class AddProduct(PermissionRequiredMixin, CreateView):
    permission_required = ('newsapp.add_post',
                           'newsapp.change_post')


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')



class NewsList(ListView):
    model = Post
    ordering = 'text'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 3


class ArticleList(ListView):
    model = Post
    ordering = 'text'
    template_name = 'article_list.html'
    context_object_name = 'article'
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


def news_list(request):
    news = Post.objects.filter(post_type=Post.NEWS).order_by('-created_at')
    return render(request, 'news.html', {'news': news})


def article_list(request):
    articles = Post.objects.filter(post_type=Post.ARTICLE).order_by('-created_at')
    return render(request, 'article_list.html', {'articles': articles})


def news_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'news_detail.html', {'post': post})


def articles_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'articles_detail.html', {'post': post})


def news_search(request):
    queryset = Post.objects.filter(post_type=Post.NEWS).order_by('-created_at')
    post_filter = News_filters(request.GET, queryset=queryset)

    paginator = Paginator(post_filter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news_search.html', {'page_obj': page_obj, 'filter': post_filter})


def articles_search(request):
    queryset = Post.objects.filter(post_type=Post.ARTICLE).order_by('-created_at')
    post_filter = News_filters(request.GET, queryset=queryset)

    paginator = Paginator(post_filter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'article_search.html', {'page_obj': page_obj, 'filter': post_filter})


class NewsCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news_form.html'
    success_url = reverse_lazy('news_search')

    def form_valid(self, form):
        author, created = Author.objects.get_or_create(user=self.request.user)
        form.instance.author = author
        post = form.save(commit=False)
        post.post_type = Post.NEWS
        return super().form_valid(form)


class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_search')

    def form_valid(self, form):
        author, created = Author.objects.get_or_create(user=self.request.user)
        form.instance.author = author
        post = form.save(commit=False)
        post.post_type = Post.ARTICLE
        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news_form.html'
    success_url = reverse_lazy('news_search')

    def form_valid(self, form):
        post = form.save(commit=False)
        if post.post_type != Post.NEWS:
            post.post_type = Post.NEWS
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_search')

    def form_valid(self, form):
        post = form.save(commit=False)
        if post.post_type != Post.ARTICLE:
            post.post_type = Post.ARTICLE
        return super().form_valid(form)


class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('news_search')


class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('news_search')

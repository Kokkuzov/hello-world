import django_filters
from django import forms
from .models import Post, Category


class News_filters(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='по названию')
    categories = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='по категориям'
    )
    created_at = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Позже')


    class Meta:
        model = Post
        fields = ['title', 'categories', 'created_at']


class Articles_filters(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='по названию')
    categories = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='по категориям')
    created_at = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Позже')


    class Meta:
        model = Post
        fields = ['title', 'categories', 'created_at']
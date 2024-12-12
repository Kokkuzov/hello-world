import django_filters
from django import forms
from django_filters import FilterSet
from .models import Post, Category
from django.forms.widgets import SelectDateWidget
from django.forms import DateInput
from django.forms.widgets import SplitDateTimeWidget
from django.forms.widgets import TextInput


class News_filters(django_filters.FilterSet):
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
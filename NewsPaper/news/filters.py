import django_filters

from django_filters import FilterSet
from .models import Post
from django.forms import widgets


class PostFilter(FilterSet):
    model = Post
    creating_dt = django_filters.DateTimeFilter(field_name='creating_dt', label='Дата:',
                                                widget=widgets.SelectDateWidget(),
                                                lookup_expr='gte', )
    name = django_filters.CharFilter(field_name='title', label='Название:',
                                     lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__user__username', label='Автор:',
                                       lookup_expr='icontains')

    class Meta:
        model = Post
        fields = {}

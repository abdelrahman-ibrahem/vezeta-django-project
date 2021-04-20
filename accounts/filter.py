import django_filters
from .models import Profile

class Filter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains' , label="الاسم")
    class Meta:
        model = Profile
        fields = ['title']


import django_filters
from power.models import *

from django_filters import CharFilter


class VacancyFilter(django_filters.FilterSet):
    title_contains = CharFilter(field_name='title',
                                   lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = ""









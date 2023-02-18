import datetime

import django_filters
from django.db.models import Sum

from users.models import User

from django_filters import rest_framework as filters

FILTER_CHOICES = (
    ('day', 'day'),
    ('year', 'year'),
    ('month', 'month'),
)


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    ...


class SaveContactCountFilter(filters.FilterSet):
    count_filter_period = django_filters.ChoiceFilter(method='filter_data', choices=FILTER_CHOICES)

    # data = CharFilterInFilter(method='filter_data', lookup_expr='in')

    class Meta:
        model = User
        fields = ('count_filter_period',)

    def filter_data(self, queryset, value, obj):

        day_date = datetime.datetime.now() - datetime.timedelta(days=1)
        month_date = datetime.datetime.now() - datetime.timedelta(days=30)
        year = datetime.datetime.now() - datetime.timedelta(days=365)
        if obj == 'day':
            queryset = User.objects.filter(save_contact_user__created_at__gte=day_date).annotate(
                total_count=Sum('save_contact_user__count'))
        elif obj == 'month':
            queryset = User.objects.filter(save_contact_user__created_at__gte=month_date).annotate(
                total_count=Sum('save_contact_user__count'))
        elif obj == 'year':
            queryset = User.objects.filter(save_contact_user__created_at__gte=year).annotate(
                total_count=Sum('save_contact_user__count'))
        else:
            return 'incorrect filter choice day week or month'
        return queryset

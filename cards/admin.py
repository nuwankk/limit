from django.contrib import admin
from django.utils.safestring import mark_safe

from cards.models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'price_dollar', 'color', 'get_image');
    list_display_links = ('price_dollar', 'color', 'get_image');

    def get_image(self, object):
        return mark_safe(f"<img src='{object.image.url}' width='50' />");


admin.site.register(Card, CardAdmin);
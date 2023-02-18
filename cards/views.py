from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail

from rest_framework import generics, views
from rest_framework.response import Response

from cards.choices import CURRENCY_TITLE
from cards.models import Card
from cards.serializers import CardSerializer


class CardListView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardOrderView(views.APIView):
    def post(self, request):
        phone = request.data.get('phone');
        location = request.data.get('location');
        order = request.data.get('order');
        order_info = "";
        dollar_total_price = 0;
        dirham_total_price = 0;
        for item in order:
            card = Card.objects.get(pk=item['id']);
            serializer = CardSerializer(card).data;
            order_info += f'Название={serializer["title"]}; Количество={item["count"]}; Цена в долларах={serializer["price_dollar"]}; Цена в дирхамах={serializer["price_dirham"]}';
            dollar_total_price += serializer['price_dollar'];
            dirham_total_price += serializer['price_dirham'];
        date = timezone.now();
        send_mail(
            'Заказ',
            f'Телефон:{phone}\nМесто:{location}\nДата:{date}\n{order_info}\n\n Общяя цена в долларах: {dollar_total_price}$\n\n Общяя цена в дирхамах: {dirham_total_price}د. إ',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return Response();

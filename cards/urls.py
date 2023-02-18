from django.urls import path

from cards.views import CardListView, CardOrderView

urlpatterns = [
    path('', CardListView.as_view()),
    path('order/', CardOrderView.as_view()),
]
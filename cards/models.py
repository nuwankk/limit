from django.db import models
from colorfield.fields import ColorField

from utils.rename import Rename

imageRename = Rename('images/cards')


class Card(models.Model):
    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        return self.title;

    title = models.CharField(max_length=300)
    color = ColorField(format='hexa')
    text_color = ColorField(format='hexa')
    image = models.ImageField(upload_to=imageRename.rename)
    price_dollar = models.FloatField()
    price_dirham = models.FloatField()

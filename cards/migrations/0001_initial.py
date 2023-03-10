# Generated by Django 4.0.1 on 2022-02-07 16:46

import colorfield.fields
from django.db import migrations, models
import utils.rename


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('color', colorfield.fields.ColorField(default='#FFFFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Цвет')),
                ('text_color', colorfield.fields.ColorField(default='#FFFFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Цвет текста')),
                ('image', models.ImageField(upload_to=utils.rename.Rename.rename, verbose_name='Фото')),
                ('price_dollar', models.FloatField(verbose_name='Цена в долларах')),
                ('price_dirham', models.FloatField(verbose_name='Цена в дирхамах')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
    ]
# Generated by Django 3.2.9 on 2022-12-06 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.rename


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220523_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='count_filter_period',
            field=models.CharField(choices=[('day', 'day'), ('month', 'month'), ('year', 'year')], default='day', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='otherWebsite',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='workEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=utils.rename.Rename.rename),
        ),
        migrations.AlterField(
            model_name='user',
            name='bg',
            field=models.ImageField(blank=True, null=True, upload_to=utils.rename.Rename.rename),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$NsxEgxpwVmfzrPQ70Qp2Pa$VtGXW6omzmHyoRKBhznPIBl6TC5YRr3L7kei4hV4378=', max_length=128),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=utils.rename.Rename.rename),
        ),
        migrations.CreateModel(
            name='SaveContactCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save_contact_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

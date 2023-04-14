# Generated by Django 4.1.4 on 2023-04-07 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='id',
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

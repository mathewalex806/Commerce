# Generated by Django 4.1.4 on 2023-04-01 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listing_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='user_created',
            field=models.ForeignKey(default='mathewalex', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
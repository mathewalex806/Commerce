# Generated by Django 4.1.4 on 2023-04-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_listing_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='user_created',
            field=models.CharField(default='mathewalex', max_length=20),
        ),
    ]
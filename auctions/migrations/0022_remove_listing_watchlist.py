# Generated by Django 4.1.4 on 2023-04-07 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_listing_watchlist_alter_listing_listing_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
    ]

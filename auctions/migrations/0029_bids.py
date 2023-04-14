# Generated by Django 4.1.4 on 2023-04-09 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('bid_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auctions.listing')),
                ('bid_amount', models.FloatField()),
                ('bid_status', models.BooleanField(default=True)),
                ('bid_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
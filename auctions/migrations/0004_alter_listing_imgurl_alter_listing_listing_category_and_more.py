# Generated by Django 4.1.4 on 2023-04-01 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_category_alter_listing_listing_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='imgurl',
            field=models.CharField(default='https://icon-library.com/images/no-picture-available-icon/no-picture-available-icon-1.jpg', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_category',
            field=models.ForeignKey(default='Custom', null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_desc',
            field=models.CharField(max_length=500),
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-27 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_initial'),
        ('bids', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='winning_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_auction', to='bids.bid'),
        ),
    ]

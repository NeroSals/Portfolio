# Generated by Django 3.0.6 on 2021-12-08 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0038_auto_20211208_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msa',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 8, 14, 33, 53, 868065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='r_request',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 8, 14, 33, 53, 869069, tzinfo=utc)),
        ),
    ]

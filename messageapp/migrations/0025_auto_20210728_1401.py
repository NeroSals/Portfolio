# Generated by Django 3.0.6 on 2021-07-28 17:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0024_auto_20210728_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msa',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 17, 1, 12, 61143, tzinfo=utc)),
        ),
    ]

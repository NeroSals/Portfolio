# Generated by Django 3.0.6 on 2021-07-28 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0022_auto_20210728_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msa',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 12, 46, 15, 503141)),
        ),
    ]

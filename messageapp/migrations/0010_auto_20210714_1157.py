# Generated by Django 3.0.6 on 2021-07-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0009_auto_20210714_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msa',
            name='time',
            field=models.DateTimeField(blank=True, verbose_name='2021-07-14 11:57'),
        ),
    ]

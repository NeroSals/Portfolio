# Generated by Django 3.0.6 on 2022-02-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0046_auto_20220207_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='msa',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]

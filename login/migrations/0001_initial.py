# Generated by Django 3.0.6 on 2021-02-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usersdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=64)),
                ('l_name', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]

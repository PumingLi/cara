# Generated by Django 2.2 on 2019-04-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190428_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='popular',
            field=models.FloatField(default=3),
        ),
    ]
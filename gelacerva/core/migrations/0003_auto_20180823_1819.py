# Generated by Django 2.1 on 2018-08-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180806_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='desired_temp',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='devices',
            name='set_point',
            field=models.FloatField(default=0),
        ),
    ]

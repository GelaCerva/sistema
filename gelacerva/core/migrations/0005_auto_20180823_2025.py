# Generated by Django 2.1 on 2018-08-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180823_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='bandwith',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='devices',
            name='control_type',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='devices',
            name='max_temp',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='devices',
            name='min_temp',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='devices',
            name='relay_state',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='devices',
            name='sm_mode',
            field=models.BooleanField(default=0),
        ),
    ]

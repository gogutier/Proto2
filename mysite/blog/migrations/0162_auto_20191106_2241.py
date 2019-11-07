# Generated by Django 2.0.13 on 2019-11-07 01:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0161_auto_20191106_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='idprogcorr',
            name='area',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 1, 41, 44, 782427, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 1, 41, 44, 782427, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 1, 41, 44, 784427, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 1, 41, 44, 784427, tzinfo=utc)),
        ),
    ]

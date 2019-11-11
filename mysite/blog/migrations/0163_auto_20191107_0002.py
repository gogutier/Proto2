# Generated by Django 2.0.13 on 2019-11-07 03:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0162_auto_20191106_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_proy_wip',
            name='M2Inv',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 3, 2, 34, 974842, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 3, 2, 34, 974842, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 3, 2, 34, 977842, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 3, 2, 34, 977842, tzinfo=utc)),
        ),
    ]
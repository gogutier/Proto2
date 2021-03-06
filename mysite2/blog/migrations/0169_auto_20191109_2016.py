# Generated by Django 2.0.13 on 2019-11-09 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0168_auto_20191109_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtroentradawip',
            name='EVENTDATETIME',
            field=models.CharField(default='0', max_length=32),
        ),
        migrations.AlterField(
            model_name='filtrosalidawip',
            name='EVENTDATETIME',
            field=models.CharField(default='0', max_length=32),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 16, 7, 242146), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 16, 7, 241146)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 16, 7, 241146)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 16, 7, 238146)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 16, 7, 242146)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 9, 20, 16, 7, 242146)),
        ),
    ]

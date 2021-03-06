# Generated by Django 2.0.13 on 2019-08-21 20:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0106_auto_20190821_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 8, 21, 20, 35, 18, 631714, tzinfo=utc), max_length=10),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 21, 20, 35, 18, 630714, tzinfo=utc), unique=True),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 21, 20, 35, 18, 632714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 8, 21, 20, 35, 18, 638715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 21, 20, 35, 18, 630714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 21, 20, 35, 18, 630714, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pruebamod',
            name='dato1',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 2.0.13 on 2019-10-16 03:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0153_remove_palletcic_ancho'),
    ]

    operations = [
        migrations.AddField(
            model_name='pallet',
            name='ORDERID',
            field=models.CharField(default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 10, 16, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 10, 16, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 10, 16, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 10, 16, 0, 0, tzinfo=utc)),
        ),
    ]
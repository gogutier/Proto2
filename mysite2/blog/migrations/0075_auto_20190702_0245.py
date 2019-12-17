# Generated by Django 2.2.2 on 2019-07-02 02:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0074_auto_20190702_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='Patente',
            field=models.CharField(default='vacio', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 2, 45, 29, 511742, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 2, 45, 29, 516972, tzinfo=utc)),
        ),
    ]

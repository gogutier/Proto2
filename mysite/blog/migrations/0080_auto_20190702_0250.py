# Generated by Django 2.2.2 on 2019-07-02 02:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0079_auto_20190702_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='camion',
            name='Chofer',
            field=models.CharField(default='vacio', max_length=10),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 2, 50, 11, 372643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 2, 50, 11, 377917, tzinfo=utc)),
        ),
    ]

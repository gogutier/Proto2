# Generated by Django 2.2.2 on 2019-07-09 05:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0085_auto_20190709_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='infowip',
            name='M2CORR',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='infowip',
            name='M2DIM',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='infowip',
            name='PiCORR',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='infowip',
            name='PiDIM',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 5, 57, 21, 994164, tzinfo=utc), max_length=10),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 5, 57, 21, 994741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 5, 57, 21, 999942, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.0.13 on 2019-09-04 02:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0134_auto_20190902_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='movpallets',
            name='ancho',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movpallets',
            name='largo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movpallets',
            name='m2uni',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movpallets',
            name='pesouni',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movpallets',
            name='unidades',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 9, 4, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 9, 4, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 9, 4, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 9, 4, 0, 0, tzinfo=utc)),
        ),
    ]

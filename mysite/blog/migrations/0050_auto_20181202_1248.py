# Generated by Django 2.0.5 on 2018-12-02 15:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_auto_20181126_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleprogcorr',
            name='datosinferior',
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2018, 12, 2, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 12, 2, 15, 48, 54, 479834, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2018, 12, 2, 0, 0, tzinfo=utc)),
        ),
    ]

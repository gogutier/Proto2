# Generated by Django 2.0.5 on 2018-11-22 23:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20181122_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2018, 11, 22, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 11, 22, 23, 7, 24, 989689, tzinfo=utc)),
        ),
    ]

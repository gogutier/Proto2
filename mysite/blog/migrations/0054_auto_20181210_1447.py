# Generated by Django 2.0.5 on 2018-12-10 17:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0053_auto_20181210_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 12, 10, 17, 47, 38, 447123, tzinfo=utc)),
        ),
    ]

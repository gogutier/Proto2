# Generated by Django 2.0.5 on 2018-10-16 03:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181016_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 10, 16, 0, 18, 48, 703005)),
        ),
    ]

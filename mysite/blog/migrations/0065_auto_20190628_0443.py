# Generated by Django 2.2.2 on 2019-06-28 04:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0064_auto_20190628_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 4, 43, 41, 618926, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 6, 28, 4, 43, 41, 624095, tzinfo=utc)),
        ),
    ]
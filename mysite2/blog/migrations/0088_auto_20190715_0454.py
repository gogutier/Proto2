# Generated by Django 2.2.2 on 2019-07-15 04:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0087_auto_20190715_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 7, 15, 4, 54, 20, 474608, tzinfo=utc), max_length=10),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 4, 54, 20, 475681, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 7, 15, 4, 54, 20, 480446, tzinfo=utc)),
        ),
    ]

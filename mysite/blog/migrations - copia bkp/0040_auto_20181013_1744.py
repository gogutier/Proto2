# Generated by Django 2.0.5 on 2018-10-13 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20181013_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargaproducciones',
            name='fecha_carga',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

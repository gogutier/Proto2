# Generated by Django 2.0.13 on 2019-09-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0142_auto_20190910_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobinvcic',
            name='nbobina',
            field=models.CharField(default='', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='pruebamod',
            name='dato2',
            field=models.CharField(max_length=10),
        ),
    ]

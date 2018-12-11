# Generated by Django 2.0.5 on 2018-11-27 02:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_auto_20181126_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semanas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField(default='1')),
                ('mescorto', models.CharField(default='vacio', max_length=10)),
                ('mesnum', models.IntegerField(default=0)),
                ('diasprod', models.FloatField(default=5.5)),
                ('año', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 11, 27, 2, 45, 12, 198093, tzinfo=utc)),
        ),
    ]

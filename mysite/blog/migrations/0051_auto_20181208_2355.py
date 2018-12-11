# Generated by Django 2.0.5 on 2018-12-09 02:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0050_auto_20181202_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoInventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_carga', models.DateField(default=datetime.datetime(2018, 12, 9, 0, 0, tzinfo=utc))),
                ('total_kraft', models.IntegerField(default=0)),
                ('total_blanco', models.IntegerField(default=0)),
                ('total_CPP', models.IntegerField(default=0)),
                ('total_otros', models.IntegerField(default=0)),
                ('kraft_saldos_kg', models.IntegerField(default=0)),
                ('blanco_saldos_kg', models.IntegerField(default=0)),
                ('CPP_saldos_kg', models.IntegerField(default=0)),
                ('otros_saldos_kg', models.IntegerField(default=0)),
                ('kraft_saldos_un', models.IntegerField(default=0)),
                ('blanco_saldos_un', models.IntegerField(default=0)),
                ('CPP_saldos_un', models.IntegerField(default=0)),
                ('otros_saldos_un', models.IntegerField(default=0)),
                ('kraft_retenidos_un', models.IntegerField(default=0)),
                ('blanco_retenidos_un', models.IntegerField(default=0)),
                ('CPP_retenidos_un', models.IntegerField(default=0)),
                ('otros_retenidos_un', models.IntegerField(default=0)),
                ('kraft_retenidos_kg', models.IntegerField(default=0)),
                ('blanco_retenidos_kg', models.IntegerField(default=0)),
                ('CPP_retenidos_kg', models.IntegerField(default=0)),
                ('otros_retenidos_kg', models.IntegerField(default=0)),
                ('kraft_3_meses', models.IntegerField(default=0)),
                ('blanco_3_meses', models.IntegerField(default=0)),
                ('CPP_3_meses', models.IntegerField(default=0)),
                ('otros_3_meses', models.IntegerField(default=0)),
                ('kraft_6_meses', models.IntegerField(default=0)),
                ('blanco_6_meses', models.IntegerField(default=0)),
                ('CPP_6_meses', models.IntegerField(default=0)),
                ('otros_6_meses', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2018, 12, 9, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 12, 9, 2, 55, 41, 122048, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2018, 12, 9, 0, 0, tzinfo=utc)),
        ),
    ]

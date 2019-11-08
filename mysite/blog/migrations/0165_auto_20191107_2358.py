# Generated by Django 2.0.13 on 2019-11-08 02:58

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0164_auto_20191107_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_MovPallets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_fin', models.DateTimeField(default=django.utils.timezone.now)),
                ('turno', models.CharField(default='0', max_length=16)),
                ('label', models.CharField(default='0', max_length=16)),
                ('M2Conv', models.FloatField(default=0)),
                ('M2Corr', models.FloatField(default=0)),
                ('M2Inv', models.FloatField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='datos_proy_wip',
            old_name='fecha_fin',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='datos_proy_wip',
            old_name='M2Conv',
            new_name='m2In',
        ),
        migrations.RenameField(
            model_name='datos_proy_wip',
            old_name='M2Corr',
            new_name='m2Out',
        ),
        migrations.RenameField(
            model_name='datos_proy_wip',
            old_name='M2Inv',
            new_name='m2Prod',
        ),
        migrations.RemoveField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
        ),
        migrations.AddField(
            model_name='datos_proy_wip',
            name='cantidadIn',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_proy_wip',
            name='cantidadOut',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_proy_wip',
            name='cantidadProd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 11, 8, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 11, 8, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 8, 2, 58, 49, 346260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 8, 2, 58, 49, 346260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 8, 2, 58, 49, 348260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 8, 2, 58, 49, 348260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 11, 8, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 11, 8, 0, 0, tzinfo=utc)),
        ),
    ]

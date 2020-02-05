# Generated by Django 2.0.13 on 2020-02-05 03:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0203_auto_20200204_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movscorrop1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movscorrop2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movscorrop3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movscorrop4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movscorrop5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movscorrop6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movscorrop7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='op1',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='op2',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='op3',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='op4',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='op5',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='op6',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='op7',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 371469), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 343469)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 355469)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 355469)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 356469)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 356469)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpalletB', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 357469)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 357469)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 342469)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 350469), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 354469), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 345469)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 370469), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 0, 0)),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 368469), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 369469)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 369469)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 372469)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 364469)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 365469)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 344469)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 370469)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 370469)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 0, 0)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 362469)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 362469)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 359469)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2020, 2, 5, 0, 0)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 5, 38, 359469)),
        ),
    ]

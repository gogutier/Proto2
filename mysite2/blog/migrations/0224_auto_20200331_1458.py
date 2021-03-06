# Generated by Django 2.0.13 on 2020-03-31 17:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0223_auto_20200330_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertabot',
            name='fechaalerta',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 10339)),
        ),
        migrations.AlterField(
            model_name='alertabot',
            name='fechaevento',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 10339)),
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 49341), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 11339)),
        ),
        migrations.AlterField(
            model_name='datos_kpi_diario',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 3, 31, 0, 0)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 20339)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 20339)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 21339)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 21339)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpalletB', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_c',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpalletC', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 27340)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 27340)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2020, 3, 31, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 11339)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 16339), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 20339), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 13339)),
        ),
        migrations.AlterField(
            model_name='foto_kpi',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 24339), unique=True),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 35340), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2020, 3, 31, 0, 0)),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 34340), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 35340)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 35340)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 50341)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 31340)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 12339)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 36340)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 36340)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2020, 3, 31, 0, 0)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacamion',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 30340)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 30340)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechapll',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 30340)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 30340)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 29340)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2020, 3, 31, 0, 0)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 14, 58, 8, 28340)),
        ),
    ]

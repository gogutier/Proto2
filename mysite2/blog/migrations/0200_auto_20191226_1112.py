# Generated by Django 2.0.13 on 2019-12-26 14:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0199_auto_20191214_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 188913), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 171913)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 178913)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 178913)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 179913)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 179913)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpalletB', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 179913)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 179913)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 12, 26, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 170913)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 175913), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 177913), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 172913)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 186913), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 12, 26, 0, 0)),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 185913), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 185913)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 185913)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 188913)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 183913)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 172913)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 187913)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 187913)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 12, 26, 0, 0)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 182913)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 182913)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 181913)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 12, 26, 0, 0)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 11, 12, 26, 180913)),
        ),
    ]

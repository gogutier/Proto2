# Generated by Django 2.0.13 on 2020-02-04 17:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0199_auto_20200204_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datos_movpallets',
            old_name='m2Prod',
            new_name='m2DirectoConv',
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 979163), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 961161)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 969162)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 969162)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 970162)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 970162)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpalletB', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 970162)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 970162)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 960161)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 966161), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 968162), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 963161)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 977162), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 976162), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 977162)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 977162)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 980163)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 974162)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 962161)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 978163)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 978163)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 973162)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 973162)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 972162)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 26, 34, 971162)),
        ),
    ]

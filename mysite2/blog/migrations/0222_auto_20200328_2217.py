# Generated by Django 2.0.13 on 2020-03-29 01:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0221_auto_20200328_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='pallet',
            name='remision',
            field=models.CharField(default='vacio', max_length=16),
        ),
        migrations.AlterField(
            model_name='alertabot',
            name='fechaalerta',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 241791)),
        ),
        migrations.AlterField(
            model_name='alertabot',
            name='fechaevento',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 241791)),
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 281793), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 243791)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 256792)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 256792)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 257792)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 257792)),
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
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 264792)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 264792)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 242791)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 250792), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 255792), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 245791)),
        ),
        migrations.AlterField(
            model_name='foto_kpi',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 262792), unique=True),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 278793), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 275793), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 275793)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 275793)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 282794)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 271793)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 245791)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 279793)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 279793)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacamion',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 268793)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 268793)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechapll',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 268793)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 268793)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 267793)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 22, 17, 2, 266793)),
        ),
    ]
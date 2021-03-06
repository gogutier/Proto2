# Generated by Django 2.0.13 on 2020-03-24 21:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0218_auto_20200324_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertabot',
            name='nombre',
            field=models.CharField(default='vacio', max_length=16),
        ),
        migrations.AlterField(
            model_name='alertabot',
            name='fechaalerta',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 464849)),
        ),
        migrations.AlterField(
            model_name='alertabot',
            name='fechaevento',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 464849)),
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 488850), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 465849)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 473849)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 473849)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 474849)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 474849)),
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
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 478849)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 478849)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 465849)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 470849), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 473849), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 467849)),
        ),
        migrations.AlterField(
            model_name='foto_kpi',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 477849), unique=True),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 486850), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 484850), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 484850)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 484850)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 489850)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 482850)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 466849)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 487850)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 487850)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacamion',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 481850)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 481850)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechapll',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 481850)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 481850)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 480849)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 18, 18, 9, 479849)),
        ),
    ]

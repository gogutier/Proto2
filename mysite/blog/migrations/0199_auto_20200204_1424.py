# Generated by Django 2.0.13 on 2020-02-04 17:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0198_auto_20191231_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datos_movpallets',
            old_name='cantidadProd',
            new_name='cantidadDirectoConv',
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 538220), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 509217)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 519218)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 520218)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 521218)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 521218)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpalletB', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 522218)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 522218)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 507217)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 514217), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 519218), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 510217)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 535219), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 0, 0)),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 532219), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 533219)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 533219)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 539220)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 529219)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 510217)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 536219)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 536219)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 0, 0)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 527219)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 527219)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 525218)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2020, 2, 4, 0, 0)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 4, 14, 24, 45, 524218)),
        ),
    ]

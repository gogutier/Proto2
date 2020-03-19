# Generated by Django 2.0.13 on 2020-03-16 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0213_auto_20200303_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsaCalles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 656843), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 632843)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 640843)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 641843)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 641843)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 641843)),
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
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 644843)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 644843)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2020, 3, 16, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 631843)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 637843), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 640843), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 634843)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 652843), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2020, 3, 16, 0, 0)),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 651843), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 651843)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 651843)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 657843)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 649843)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 633843)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 653843)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 653843)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2020, 3, 16, 0, 0)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacamion',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 647843)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 647843)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechapll',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 647843)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 647843)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 646843)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2020, 3, 16, 0, 0)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 10, 1, 58, 645843)),
        ),
    ]

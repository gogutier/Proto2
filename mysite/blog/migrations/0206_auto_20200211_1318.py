# Generated by Django 2.0.13 on 2020-02-11 16:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0205_auto_20200211_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsconvop1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsconvop2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsconvop3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsconvop4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsconvop5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsconvop6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='movsconvop7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='opconv1',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='opconv2',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='opconv3',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='opconv4',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='opconv5',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='opconv6',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AddField(
            model_name='datos_movpallets_b',
            name='opconv7',
            field=models.CharField(default='0', max_length=26),
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 958327), max_length=10),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 937325)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 946326)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 946326)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 947326)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 947326)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets_b',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpalletB', to='blog.Foto_Datos_MovPallets'),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 948326)),
        ),
        migrations.AlterField(
            model_name='datos_proy_wip',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 948326)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 936325)),
        ),
        migrations.AlterField(
            model_name='foto_datos_inv_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 942325), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_datos_movpallets',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 945326), unique=True),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 939325)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 956327), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoprogcorr',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 955327), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 955327)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 955327)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 959327)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 952326)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 953327)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 939325)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 957327)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 957327)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechacreac',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 951326)),
        ),
        migrations.AlterField(
            model_name='pallet',
            name='fechaultmov',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 951326)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='fechatoma',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 950326)),
        ),
        migrations.AlterField(
            model_name='tomainvcic',
            name='fechatomainvcic',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 13, 18, 13, 949326)),
        ),
    ]

# Generated by Django 2.0.13 on 2019-11-22 03:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0190_auto_20191118_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto_Datos_Movpallets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_foto', models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 926443), unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 914442)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 927443)),
        ),
        migrations.AlterField(
            model_name='datos_movpallets',
            name='fechafin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 927443)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 11, 22, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 913442)),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 915442)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 940444), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 11, 22, 0, 0)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 938444)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 938444)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 935443)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 915442)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 941444)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 22, 0, 15, 20, 941444)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 11, 22, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 11, 22, 0, 0, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='datos_movpallets',
            name='programa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_datosmovpallet', to='blog.Foto_Datos_Movpallets'),
        ),
    ]

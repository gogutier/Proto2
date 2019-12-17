# Generated by Django 2.0.13 on 2019-11-17 03:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0186_auto_20191116_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto_ConsumoRollos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_foto', models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 71278))),
                ('turno', models.CharField(default='0', max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 72278)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 11, 17, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 73278)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 88279), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 11, 17, 0, 0)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 87279)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 87279)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 84279)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 73278)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 88279)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 0, 2, 6, 88279)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 11, 17, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 11, 17, 0, 0, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='consumorollos',
            name='foto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_consrollos', to='blog.Foto_ConsumoRollos'),
        ),
    ]

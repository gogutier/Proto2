# Generated by Django 2.0.13 on 2019-11-18 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0189_auto_20191117_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='movrollos',
            name='destinoaux',
            field=models.CharField(default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 624887)),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 0, 0)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 623887)),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 625887)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 639887), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 0, 0)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 638887)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 638887)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 635887)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 625887)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 639887)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 10, 16, 0, 639887)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 0, 0, tzinfo=utc)),
        ),
    ]

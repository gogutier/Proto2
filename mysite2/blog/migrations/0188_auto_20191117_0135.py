# Generated by Django 2.0.13 on 2019-11-17 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0187_auto_20191117_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto_consumorollos',
            name='label',
            field=models.CharField(default='0', max_length=16),
        ),
        migrations.AlterField(
            model_name='consumorollos',
            name='fechaini',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 358253)),
        ),
        migrations.AlterField(
            model_name='foto_consumorollos',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 357253)),
        ),
        migrations.AlterField(
            model_name='foto_inv_cic_wip',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 359253)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 374254), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 373254)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 373254)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 370254)),
        ),
        migrations.AlterField(
            model_name='movrollos',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 359253)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 374254)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 1, 35, 20, 374254)),
        ),
    ]
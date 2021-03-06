# Generated by Django 2.2.2 on 2019-08-20 01:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0103_auto_20190819_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='BobInvCic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbobina', models.CharField(default='vacio', max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='camion',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 8, 20, 1, 34, 30, 689952, tzinfo=utc), max_length=10),
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 8, 20, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 1, 34, 30, 688261, tzinfo=utc), unique=True),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 8, 20, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='infowip',
            name='fechamuestra',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 1, 34, 30, 690494, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2019, 8, 20, 1, 34, 30, 695219, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 1, 34, 30, 688592, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 1, 34, 30, 688614, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 8, 20, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 8, 20, 0, 0, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.0.13 on 2019-10-31 19:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0155_auto_20191028_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosWIP_Prog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maquina', models.CharField(default='0', max_length=6)),
                ('m2Prog24', models.FloatField(default=0)),
                ('m2EnInv', models.FloatField(default=0)),
                ('m224h', models.FloatField(default=0)),
                ('indice', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='diaconv2',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fotoinventario',
            name='fecha_carga',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 19, 30, 1, 993704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 31, 19, 30, 1, 993704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='fechacarga',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='palletcic',
            name='tomainvcic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tomainv_cic', to='blog.TomaInvCic'),
        ),
        migrations.AlterField(
            model_name='proymkt',
            name='fechaproy',
            field=models.DateField(default=datetime.datetime(2019, 10, 31, 0, 0, tzinfo=utc)),
        ),
    ]
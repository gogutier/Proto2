# Generated by Django 2.0.13 on 2019-11-13 10:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0180_auto_20191113_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto_Inv_Cic_WIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_foto', models.DateTimeField(default=datetime.datetime(2019, 11, 13, 7, 41, 43, 408781))),
            ],
        ),
        migrations.AlterField(
            model_name='fotocorrplan',
            name='fecha_foto',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 7, 41, 43, 422782), unique=True),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 7, 41, 43, 421782)),
        ),
        migrations.AlterField(
            model_name='idprogcorr',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 7, 41, 43, 421782)),
        ),
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 7, 41, 43, 418782)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_entrega',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 7, 41, 43, 422782)),
        ),
        migrations.AlterField(
            model_name='ordencorrplan',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 13, 7, 41, 43, 422782)),
        ),
        migrations.AddField(
            model_name='foto_calles_inv_cic_wip',
            name='foto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='foto_invcic', to='blog.Foto_Inv_Cic_WIP'),
        ),
    ]
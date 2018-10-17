# Generated by Django 2.0.5 on 2018-10-13 20:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20181013_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargaProducciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_carga', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='prodreal',
            name='cargamasiva',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='fecha_carga_producciones', to='blog.CargaProducciones'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.5 on 2018-10-13 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodreal',
            name='cargamasivaa',
        ),
        migrations.DeleteModel(
            name='CargaProducciones',
        ),
    ]
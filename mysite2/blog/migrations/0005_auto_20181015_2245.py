# Generated by Django 2.0.5 on 2018-10-16 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181014_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleprog',
            name='datefin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='detalleprog',
            name='dateini',
            field=models.DateTimeField(),
        ),
    ]

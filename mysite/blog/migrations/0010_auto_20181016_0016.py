# Generated by Django 2.0.5 on 2018-10-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181016_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(),
        ),
    ]

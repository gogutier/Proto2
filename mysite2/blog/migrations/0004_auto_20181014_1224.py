# Generated by Django 2.0.5 on 2018-10-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181013_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleprog',
            name='qIn',
            field=models.IntegerField(default=0),
        ),
    ]

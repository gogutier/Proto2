# Generated by Django 2.0.5 on 2018-10-16 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181015_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minuta',
            old_name='integrantes',
            new_name='obs',
        ),
    ]

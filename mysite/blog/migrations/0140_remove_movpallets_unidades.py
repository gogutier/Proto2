# Generated by Django 2.0.13 on 2019-09-07 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0139_remove_movpallets_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movpallets',
            name='unidades',
        ),
    ]

# Generated by Django 2.0.13 on 2019-09-07 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0138_auto_20190907_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movpallets',
            name='cliente',
        ),
    ]
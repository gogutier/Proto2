# Generated by Django 2.0.13 on 2019-08-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0112_auto_20190830_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movpallets',
            name='EVENTDATETIME',
            field=models.DateTimeField(),
        ),
    ]
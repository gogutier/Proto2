# Generated by Django 2.0.13 on 2019-09-02 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0131_auto_20190902_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='ubic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ubic_pallet', to='blog.UbicPallet'),
        ),
    ]

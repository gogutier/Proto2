# Generated by Django 2.0.13 on 2019-10-08 23:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0150_auto_20191008_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='TomaInvCic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechatomainvcic', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='palletcic',
            name='tomainvcic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tomainv_cic', to='blog.TomaInvCic'),
        ),
    ]

# Generated by Django 2.2 on 2020-08-11 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filma', '0005_auto_20200811_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filma',
            name='network_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filma.Network'),
        ),
    ]
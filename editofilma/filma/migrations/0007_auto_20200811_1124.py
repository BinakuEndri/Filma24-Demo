# Generated by Django 2.2 on 2020-08-11 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filma', '0006_auto_20200811_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filma',
            name='network_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filma.Network'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-22 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccionip', '0002_alter_direccionip_options'),
        ('activo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='id_direccionipFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='direccionip.direccionip', unique=True),
        ),
    ]
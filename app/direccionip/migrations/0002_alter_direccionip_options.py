# Generated by Django 3.2.8 on 2021-10-22 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direccionip', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direccionip',
            options={'ordering': ['id_direccionPK'], 'verbose_name': 'Direccion', 'verbose_name_plural': 'Direccion'},
        ),
    ]

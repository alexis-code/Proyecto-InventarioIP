# Generated by Django 3.2.8 on 2021-10-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id_agenciaPK', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(default='s/c', max_length=10, verbose_name='Código de Agencia')),
                ('nombre', models.CharField(default='s/n', max_length=30, unique=True, verbose_name='Nombre de Agencia')),
                ('descripcion', models.TextField(blank=True, default='sin descripción', verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Agencia',
                'verbose_name_plural': 'Agencia',
                'db_table': 'tb_agencia',
                'ordering': ['-id_agenciaPK'],
            },
        ),
    ]

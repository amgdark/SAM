# Generated by Django 3.1.3 on 2020-12-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20201201_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidas',
            name='nombre_partida',
            field=models.CharField(max_length=200, verbose_name='Nombre de partida'),
        ),
    ]
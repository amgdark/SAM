# Generated by Django 3.1.3 on 2020-11-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='nombre_area',
            field=models.CharField(max_length=150, verbose_name='Nombre del area'),
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_auto_20201128_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='nombre_area',
            field=models.CharField(max_length=150, verbose_name='Nombre del área'),
        ),
    ]

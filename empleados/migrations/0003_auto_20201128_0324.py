# Generated by Django 3.1.3 on 2020-11-28 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20201128_0317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='appellido_materno',
            new_name='apellido_materno',
        ),
    ]

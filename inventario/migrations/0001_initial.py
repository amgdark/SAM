# Generated by Django 3.1.3 on 2020-11-27 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partidas',
            fields=[
                ('numero_partida', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Numero de partida')),
                ('nombre_partida', models.CharField(max_length=20, verbose_name='Nombre de partida')),
                ('descripcion', models.CharField(max_length=700, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre del producto')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca del producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Precio')),
                ('giro', models.CharField(max_length=100, verbose_name='Giro')),
                ('unidad', models.CharField(max_length=50, verbose_name='Unidad')),
                ('presentacion', models.CharField(max_length=100, verbose_name='Presentación')),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.partidas', verbose_name='Partida')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_factura', models.CharField(max_length=50, verbose_name='Número de factura')),
                ('fecha', models.DateField(verbose_name='Fecha de registro')),
                ('cantidad', models.IntegerField(max_length=4, verbose_name='Cantidad en stock')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.productos', verbose_name='Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Salida_productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de solicitud')),
                ('cantidad', models.IntegerField(max_length=4, verbose_name='Cantidad')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado', verbose_name='Nombre de empleado')),
                ('producto_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.stock', verbose_name='Producto')),
            ],
        ),
    ]

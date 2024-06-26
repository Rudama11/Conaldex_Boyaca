# Generated by Django 5.0.6 on 2024-06-14 12:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('Ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('Tipo_Documento', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=2)),
                ('correo', models.EmailField(default='example@example.com', max_length=250, unique=True)),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime.now, verbose_name='Fecha nacimiento')),
                ('telefono', models.IntegerField(default=True)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField(default=0)),
                ('direccion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Direccion')),
                ('Tipo_Documento', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=2)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Departamento', models.CharField(max_length=100, verbose_name='Departamento')),
                ('Ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Ubicacion',
                'verbose_name_plural': 'Ubicaciones',
                'db_table': 'Ubicacion',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('Stock', models.IntegerField(default=True)),
                ('Precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField(default=0)),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('precio_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('producto', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('proveedor', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.proveedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'Compra',
            },
        ),
        migrations.AddField(
            model_name='proveedor',
            name='cod_postal',
            field=models.ForeignKey(max_length=6, on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_Documento', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('CE', 'Cedula de extranjeria'), ('TI', 'Tarjeta de identidad')], default='CC', max_length=2)),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('correo', models.EmailField(default='example@example.com', max_length=250, unique=True)),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today, verbose_name='Fecha nacimiento')),
                ('direccion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Direccion')),
                ('telefono', models.IntegerField(default=0)),
                ('cod_postal', models.ForeignKey(max_length=6, on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Cliente',
            },
        ),
    ]

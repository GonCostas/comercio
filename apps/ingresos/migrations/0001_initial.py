# Generated by Django 5.2.1 on 2025-06-26 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remitos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_remito', models.CharField(max_length=20)),
                ('numero_viaje', models.IntegerField()),
                ('detalle_transporte', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('aprobado', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RemitoProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ingresos.productos')),
            ],
        ),
    ]

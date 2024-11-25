# Generated by Django 5.1.3 on 2024-11-24 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nom_rol', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=11)),
                ('id_rol', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestor.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id_tecnico', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=11)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_ticket', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('abierto', 'Abierto'), ('en_proceso', 'En Proceso'), ('cerrado', 'Cerrado')], default='abierto', max_length=20)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='TicketAsignado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.tecnico')),
                ('id_ticket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestor.ticket')),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2024-05-19 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parqueadero', '0002_rename_propietario_parqueaderopropietario_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parqueadero',
            name='tipo',
            field=models.CharField(choices=[('Propietario', 'Parqueadero para propietarios'), ('Visitante', 'Parqueadero para visitantes')], max_length=100, verbose_name='tipo de parqueadero'),
        ),
        migrations.AlterField(
            model_name='parqueaderopropietario',
            name='parqueadero',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parqueadero.parqueadero'),
        ),
    ]

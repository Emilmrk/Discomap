# Generated by Django 5.1.4 on 2024-12-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discoteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('capacidad', models.PositiveIntegerField(blank=True, null=True)),
                ('horario_apertura', models.TimeField(blank=True, null=True)),
                ('horario_cierre', models.TimeField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('es_activo', models.BooleanField(default=True)),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-22 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Registro'),
        ),
    ]

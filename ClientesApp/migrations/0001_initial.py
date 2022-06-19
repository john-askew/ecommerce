# Generated by Django 4.0.4 on 2022-06-15 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=100)),
                ('imagen_documento', models.ImageField(blank=True, null=True, upload_to='media_clientes')),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('validado', models.BooleanField(default=False)),
                ('nick', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

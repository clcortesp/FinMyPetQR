# Generated by Django 4.2.4 on 2023-10-05 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='mascotas')),
                ('descripcion', models.TextField(max_length=200, null=True)),
                ('detalles', models.TextField(max_length=200, null=True)),
                ('dueño', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.razamascota')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipomascota')),
            ],
        ),
    ]

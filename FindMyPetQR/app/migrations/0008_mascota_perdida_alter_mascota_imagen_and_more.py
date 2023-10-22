# Generated by Django 4.2.4 on 2023-10-09 05:30

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_descripcion_mascota_detalles_adicionales_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='perdida',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to=app.models.mascota_picture_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='imagen',
            field=models.ImageField(default='default.png', null=True, upload_to=app.models.profile_picture_path),
        ),
    ]

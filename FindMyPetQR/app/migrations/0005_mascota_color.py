# Generated by Django 4.2.4 on 2023-10-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='color',
            field=models.CharField(choices=[('Blanco', 'Blanco'), ('Negro', 'Negro'), ('Marrón', 'Marrón'), ('Gris', 'Gris'), ('Amarillo', 'Amarillo'), ('Rojo', 'Rojo'), ('Naranja', 'Naranja'), ('Crema', 'Crema'), ('Atigrado', 'Atigrado'), ('Tricolor', 'Tricolor'), ('Azul', 'Azul'), ('Beige', 'Beige'), ('Plateado', 'Plateado'), ('Dorado', 'Dorado'), ('Blanco y negro', 'Blanco y negro'), ('Blanco y marrón', 'Blanco y marrón'), ('Blanco y gris', 'Blanco y gris'), ('Negro y marrón', 'Negro y marrón'), ('Negro y blanco', 'Negro y blanco'), ('Gris y blanco', 'Gris y blanco'), ('Gris y negro', 'Gris y negro'), ('Marrón y blanco', 'Marrón y blanco'), ('Marrón y negro', 'Marrón y negro'), ('Rojo y blanco', 'Rojo y blanco'), ('Rojo y negro', 'Rojo y negro'), ('Naranja y blanco', 'Naranja y blanco'), ('Naranja y negro', 'Naranja y negro'), ('Crema y blanco', 'Crema y blanco'), ('Crema y marrón', 'Crema y marrón'), ('Atigrado marrón', 'Atigrado marrón'), ('Atigrado gris', 'Atigrado gris'), ('Atigrado negro', 'Atigrado negro'), ('Tricolor (blanco, negro y marrón)', 'Tricolor (blanco, negro y marrón)'), ('Tricolor (blanco, negro y gris)', 'Tricolor (blanco, negro y gris)'), ('Tricolor (blanco, marrón y gris)', 'Tricolor (blanco, marrón y gris)'), ('Azul y blanco', 'Azul y blanco'), ('Azul y negro', 'Azul y negro'), ('Beige y blanco', 'Beige y blanco'), ('Beige y marrón', 'Beige y marrón'), ('Plateado y blanco', 'Plateado y blanco'), ('Plateado y negro', 'Plateado y negro'), ('Dorado y blanco', 'Dorado y blanco'), ('Dorado y negro', 'Dorado y negro'), ('Blanco y naranja', 'Blanco y naranja'), ('Negro y naranja', 'Negro y naranja'), ('Marrón y naranja', 'Marrón y naranja'), ('Gris y naranja', 'Gris y naranja')], max_length=50, null=True),
        ),
    ]

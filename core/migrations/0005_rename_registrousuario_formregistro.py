# Generated by Django 4.0.4 on 2023-05-05 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_apellido_registrousuario_apellidos_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegistroUsuario',
            new_name='formRegistro',
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_rename_picture_compra_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='estado_orden',
            field=models.CharField(choices=[('', '----'), ('Bloqueada', 'Bloqueada'), ('Aceptada', 'Aceptada'), ('Pendiente', 'Pendiente')], default='', max_length=200),
        ),
    ]

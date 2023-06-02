# Generated by Django 4.2.1 on 2023-05-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_producto_tipo_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('', ''), ('Acción', 'Acción'), ('Aventura', 'Aventura'), ('Estrategia', 'Estrategia'), ('RPG', 'RPG'), ('Deportes', 'Deportes'), ('Carreras', 'Carreras'), ('Puzzle', 'Puzzle'), ('Plataformas', 'Plataformas'), ('Shooter', 'Shooter'), ('Simulación', 'Simulación')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('', ''), ('Juego', 'Juego'), ('Accesorio', 'Accesorio'), ('Juego Descargable', 'Juego Descargable')], default='', max_length=200),
        ),
    ]
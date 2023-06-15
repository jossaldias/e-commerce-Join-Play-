# Generated by Django 4.2.1 on 2023-06-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_producto_tipo_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('', '----'), ('Juego Físico', 'Juego Físico'), ('Accesorio', 'Accesorio'), ('Código Digital', 'Código Digital')], default='', max_length=200),
        ),
        migrations.AlterOrderWithRespectTo(
            name='producto',
            order_with_respect_to='tipo_producto',
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_orden', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('id_producto', models.CharField(max_length=255, null=True, unique=True)),
                ('nombre', models.CharField(max_length=255, null=True, unique=True)),
                ('proveedor', models.CharField(max_length=255, null=True, unique=True)),
                ('plataforma', models.CharField(choices=[('', '----'), ('PlayStation 5', 'PlayStation 5'), ('Xbox Series X', 'Xbox Series X'), ('Xbox 360', 'Xbox 360'), ('Nintendo Switch', 'Nintendo Switch'), ('PC Gaming', 'PC Gaming'), ('PlayStation 4', 'PlayStation 4'), ('Xbox One', 'Xbox One'), ('Nintendo 3DS', 'Nintendo 3DS'), ('Sega Genesis Mini', 'Sega Genesis Mini'), ('Super Nintendo Entertainment System (SNES) Classic Edition', 'Super Nintendo Entertainment System (SNES) Classic Edition'), ('Nintendo Entertainment System (NES) Classic Edition', 'Nintendo Entertainment System (NES) Classic Edition')], default='', max_length=200)),
                ('tipo_producto', models.CharField(choices=[('', '----'), ('Juego Físico', 'Juego Físico'), ('Accesorio', 'Accesorio'), ('Código Digital', 'Código Digital')], default='', max_length=200)),
                ('costo', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('estado_orden', models.CharField(choices=[('', '----'), ('Juego Físico', 'Juego Físico'), ('Accesorio', 'Accesorio'), ('Código Digital', 'Código Digital')], default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compra',
                'order_with_respect_to': 'id_orden',
            },
        ),
    ]
# Generated by Django 3.2.4 on 2023-06-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_item_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estado_orden',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Bloqueada', 'Bloqueada'), ('Aceptada', 'Aceptada'), ('Finalizada', 'Finalizada')], default='Pendiente', max_length=200, verbose_name='Estado Órden'),
        ),
    ]
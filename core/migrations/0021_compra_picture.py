# Generated by Django 4.2.1 on 2023-06-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_compra_options_rename_id_producto_compra_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/productos/'),
        ),
    ]

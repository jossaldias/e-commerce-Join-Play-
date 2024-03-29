# Generated by Django 3.2.4 on 2023-06-15 03:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_compra_estado_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='documento',
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=250, null=True, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=250, null=True, verbose_name='Teléfono')),
                ('descripcion', models.CharField(blank=True, max_length=250, verbose_name='Descripción')),
                ('region', models.CharField(max_length=250, null=True, verbose_name='Región')),
                ('comuna', models.CharField(max_length=250, null=True, verbose_name='Comuna')),
                ('is_pagado', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ItemProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_oc', to='core.order')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items_oc', to='core.producto')),
            ],
        ),
    ]

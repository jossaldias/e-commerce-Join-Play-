# Generated by Django 3.2.4 on 2023-06-02 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_order_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='nombre',
        ),
    ]

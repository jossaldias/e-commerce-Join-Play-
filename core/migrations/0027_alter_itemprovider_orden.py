# Generated by Django 3.2.4 on 2023-06-15 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20230615_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprovider',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_oc', to='core.orden'),
        ),
    ]

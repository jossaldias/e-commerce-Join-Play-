# Generated by Django 4.2.1 on 2023-05-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
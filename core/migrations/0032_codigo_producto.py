# Generated by Django 4.2.1 on 2023-06-20 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigo',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='codigos', to='core.producto'),
        ),
    ]

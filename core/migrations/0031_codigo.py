# Generated by Django 4.2.1 on 2023-06-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20230615_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'codigo',
                'verbose_name_plural': 'codigos',
                'order_with_respect_to': 'codigo',
            },
        ),
    ]

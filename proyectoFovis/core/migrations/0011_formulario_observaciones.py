# Generated by Django 4.1.1 on 2022-09-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_formulario_cedula_conyugue'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='observaciones',
            field=models.TextField(blank=True, max_length=100, verbose_name='Observaciones'),
        ),
    ]
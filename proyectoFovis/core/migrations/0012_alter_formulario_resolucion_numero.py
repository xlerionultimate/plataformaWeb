# Generated by Django 4.1.1 on 2022-09-29 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_formulario_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='resolucion_numero',
            field=models.CharField(max_length=100, verbose_name='Codigo de la Resolución'),
        ),
    ]

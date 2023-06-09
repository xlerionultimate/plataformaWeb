# Generated by Django 4.1.1 on 2022-09-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_formulario_resolucion_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='lugar_expedicion_informacion',
            field=models.CharField(default=0, max_length=100, verbose_name='Lugar de Expedición de la Cédula del que suministra la Información'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='apellido_suministro_de_informacion',
            field=models.CharField(max_length=100, verbose_name='Apellido de quien suministra la Información'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='edad',
            field=models.IntegerField(default=0, editable=False, unique=True, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='personas_a_cargo_jefe_hogar',
            field=models.IntegerField(blank=True, default=0, editable=False, verbose_name='Número de Personas a CArgo del Jefe de Hogar'),
        ),
    ]

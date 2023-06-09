# Generated by Django 4.1.1 on 2022-09-29 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_formulario_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria', verbose_name='Seleccione la Categoria a la que pertenece'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='composicion_familiar_nom_ape',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombres Jefe de Hogar'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='ocupacion',
            field=models.TextField(blank=True, max_length=600, verbose_name='Ocupación'),
        ),
        migrations.AlterField(
            model_name='numerohogares',
            name='name',
            field=models.DecimalField(decimal_places=0, max_digits=3, unique=True, verbose_name='Numero de Hogares en la Vivienda'),
        ),
    ]

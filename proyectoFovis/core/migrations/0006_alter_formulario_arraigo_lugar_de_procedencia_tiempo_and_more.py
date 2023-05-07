# Generated by Django 4.1.1 on 2022-09-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_formulario_numero_hogares_en_vivienda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='arraigo_lugar_de_procedencia_tiempo',
            field=models.IntegerField(blank=True, default=0, max_length=3, null=True, verbose_name='De Donde?'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='tiempo_residencia_municipio',
            field=models.IntegerField(default=0, max_length=3, null=True, verbose_name='Hace cuántos? años reside en el Municipio'),
        ),
        migrations.AlterField(
            model_name='tiempoviviendo',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Tiempo viviendo en el Municipio'),
        ),
    ]
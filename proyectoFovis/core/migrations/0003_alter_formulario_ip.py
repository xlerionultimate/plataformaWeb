# Generated by Django 4.1.1 on 2022-09-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_formulario_imagen_firma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP'),
        ),
    ]
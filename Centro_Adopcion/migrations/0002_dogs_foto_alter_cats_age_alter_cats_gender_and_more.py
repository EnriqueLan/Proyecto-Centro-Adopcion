# Generated by Django 5.0.6 on 2024-06-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Centro_Adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogs',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_mascotas'),
        ),
        migrations.AlterField(
            model_name='cats',
            name='Age',
            field=models.CharField(max_length=40, verbose_name='Edad:(Meses o Años)'),
        ),
        migrations.AlterField(
            model_name='cats',
            name='Gender',
            field=models.CharField(max_length=40, verbose_name='Genero:(Macho o Hembra)'),
        ),
        migrations.AlterField(
            model_name='cats',
            name='Name',
            field=models.CharField(max_length=40, verbose_name='Nombre:'),
        ),
        migrations.AlterField(
            model_name='cats',
            name='Race',
            field=models.CharField(max_length=40, verbose_name='Raza:'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='Age',
            field=models.CharField(max_length=40, verbose_name='Edad:(Meses o Años)'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='Gender',
            field=models.CharField(max_length=40, verbose_name='Genero:(Macho o Hembra)'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='Name',
            field=models.CharField(max_length=40, verbose_name='Nombre:'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='Race',
            field=models.CharField(max_length=40, verbose_name='Raza:'),
        ),
    ]

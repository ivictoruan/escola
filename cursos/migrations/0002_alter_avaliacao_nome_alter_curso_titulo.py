# Generated by Django 4.2.1 on 2023-05-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='curso',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
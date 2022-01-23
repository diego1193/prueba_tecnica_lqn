# Generated by Django 2.2.13 on 2022-01-21 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20220120_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='character',
            name='hair_color',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='character',
            name='skin_color',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('red', 'RED'), ('bald', 'BALD'), ('brown', 'BROWN'), ('blonde', 'BLONDE'), ('black', 'BLACK'), ('white', 'WHITE')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='skin_color',
            field=models.CharField(blank=True, choices=[('red', 'RED'), ('brown', 'BROWN'), ('yellow', 'YELLOW'), ('purple', 'PURPLE'), ('unknown', 'UNKNOW'), ('green', 'GREEN'), ('black', 'BLACK')], max_length=32),
        ),
    ]

# Generated by Django 2.2.13 on 2022-01-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220120_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('green', 'GREEN'), ('purple', 'PURPLE'), ('unknown', 'UNKNOW'), ('red', 'RED'), ('brown', 'BROWN'), ('black', 'BLACK'), ('yellow', 'YELLOW')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('white', 'WHITE'), ('blonde', 'BLONDE'), ('red', 'RED'), ('brown', 'BROWN'), ('black', 'BLACK'), ('bald', 'BALD')], max_length=32),
        ),
    ]

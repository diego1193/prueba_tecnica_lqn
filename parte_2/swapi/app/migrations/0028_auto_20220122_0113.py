# Generated by Django 2.2.13 on 2022-01-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20220122_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('white', 'WHITE'), ('unknown', 'UNKNOWN'), ('brown', 'BROWN'), ('purple', 'PURPLE'), ('yellow', 'YELLOW'), ('black', 'BLACK'), ('red', 'RED'), ('blue', 'BLUE'), ('green', 'GREEN')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('white', 'WHITE'), ('none', 'NONE'), ('brown', 'BROWN'), ('blonde', 'BLONDE'), ('red', 'RED'), ('black', 'BLACK'), ('bald', 'BALD')], max_length=32),
        ),
    ]

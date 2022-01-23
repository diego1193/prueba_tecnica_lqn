# Generated by Django 2.2.13 on 2022-01-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20220123_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('purple', 'PURPLE'), ('blue', 'BLUE'), ('yellow', 'YELLOW'), ('white', 'WHITE'), ('green', 'GREEN'), ('red', 'RED'), ('unknown', 'UNKNOWN')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('black', 'BLACK'), ('brown', 'BROWN'), ('white', 'WHITE'), ('red', 'RED'), ('blonde', 'BLONDE'), ('none', 'NONE'), ('bald', 'BALD')], max_length=32),
        ),
    ]
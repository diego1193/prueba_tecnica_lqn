# Generated by Django 2.2.13 on 2022-01-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20220122_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('brown', 'BROWN'), ('blue', 'BLUE'), ('unknown', 'UNKNOWN'), ('white', 'WHITE'), ('black', 'BLACK'), ('yellow', 'YELLOW'), ('green', 'GREEN'), ('red', 'RED'), ('purple', 'PURPLE')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('brown', 'BROWN'), ('white', 'WHITE'), ('none', 'NONE'), ('black', 'BLACK'), ('blonde', 'BLONDE'), ('bald', 'BALD'), ('red', 'RED')], max_length=32),
        ),
    ]
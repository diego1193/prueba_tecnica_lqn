# Generated by Django 2.2.13 on 2022-01-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20220120_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='films',
            field=models.ManyToManyField(blank=True, related_name='films_character', to='app.Film'),
        ),
        migrations.AlterField(
            model_name='character',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('brown', 'BROWN'), ('red', 'RED'), ('blonde', 'BLONDE'), ('bald', 'BALD'), ('white', 'WHITE'), ('black', 'BLACK')], max_length=32),
        ),
        migrations.AlterField(
            model_name='character',
            name='skin_color',
            field=models.CharField(blank=True, choices=[('brown', 'BROWN'), ('red', 'RED'), ('unknown', 'UNKNOW'), ('yellow', 'YELLOW'), ('purple', 'PURPLE'), ('green', 'GREEN'), ('black', 'BLACK')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('brown', 'BROWN'), ('red', 'RED'), ('blonde', 'BLONDE'), ('bald', 'BALD'), ('white', 'WHITE'), ('black', 'BLACK')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='skin_color',
            field=models.CharField(blank=True, choices=[('brown', 'BROWN'), ('red', 'RED'), ('unknown', 'UNKNOW'), ('yellow', 'YELLOW'), ('purple', 'PURPLE'), ('green', 'GREEN'), ('black', 'BLACK')], max_length=32),
        ),
    ]
# Generated by Django 2.2.13 on 2022-01-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220120_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('brown', 'BROWN'), ('bald', 'BALD'), ('white', 'WHITE'), ('red', 'RED'), ('black', 'BLACK'), ('blonde', 'BLONDE')], max_length=32),
        ),
    ]

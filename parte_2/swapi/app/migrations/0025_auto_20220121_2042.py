# Generated by Django 2.2.13 on 2022-01-22 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20220120_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='skin_color',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
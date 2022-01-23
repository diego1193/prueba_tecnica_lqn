# Generated by Django 2.2.13 on 2022-01-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220120_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('hermaphrodite', 'Hermaphrodite'), ('n/a', 'N/A')], max_length=64),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]

# Generated by Django 2.2.13 on 2022-01-20 18:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220120_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('unknown', 'UNKNOW'), ('red', 'RED'), ('purple', 'PURPLE'), ('yellow', 'YELLOW'), ('black', 'BLACK'), ('brown', 'BROWN'), ('green', 'GREEN')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('red', 'RED'), ('bald', 'BALD'), ('blonde', 'BLONDE'), ('black', 'BLACK'), ('brown', 'BROWN'), ('white', 'WHITE')], max_length=32),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=128)),
                ('height', models.CharField(blank=True, max_length=16)),
                ('mass', models.CharField(blank=True, max_length=16)),
                ('hair_color', models.CharField(blank=True, choices=[('red', 'RED'), ('bald', 'BALD'), ('blonde', 'BLONDE'), ('black', 'BLACK'), ('brown', 'BROWN'), ('white', 'WHITE')], max_length=32)),
                ('skin_color', models.CharField(blank=True, max_length=32)),
                ('eye_color', models.CharField(blank=True, choices=[('unknown', 'UNKNOW'), ('red', 'RED'), ('purple', 'PURPLE'), ('yellow', 'YELLOW'), ('black', 'BLACK'), ('brown', 'BROWN'), ('green', 'GREEN')], max_length=32)),
                ('birth_year', models.CharField(blank=True, max_length=16)),
                ('gender', models.CharField(blank=True, max_length=64)),
                ('film', models.ManyToManyField(blank=True, related_name='films_characters', to='app.Planet')),
                ('home_world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inhabitants_create', to='app.Planet')),
            ],
            options={
                'verbose_name_plural': 'character',
                'db_table': 'character',
            },
        ),
    ]

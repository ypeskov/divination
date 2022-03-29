# Generated by Django 4.0.3 on 2022-03-28 08:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('runes', '0003_alter_divination_description_alter_rune_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(max_length=20)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('forecast_meaning_direct', tinymce.models.HTMLField(blank=True)),
                ('forecast_meaning_inverted', tinymce.models.HTMLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runes.rune')),
            ],
        ),
    ]
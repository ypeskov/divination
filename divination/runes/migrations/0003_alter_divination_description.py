# Generated by Django 4.0.3 on 2022-03-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runes', '0002_rename_name_divination_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divination',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

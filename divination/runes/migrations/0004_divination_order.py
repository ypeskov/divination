# Generated by Django 4.0.3 on 2022-03-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runes', '0003_alter_divination_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='divination',
            name='order',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]

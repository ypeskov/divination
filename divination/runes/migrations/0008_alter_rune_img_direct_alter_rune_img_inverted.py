# Generated by Django 4.0.3 on 2022-03-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runes', '0007_alter_rune_img_direct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rune',
            name='img_direct',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rune',
            name='img_inverted',
            field=models.URLField(blank=True, null=True),
        ),
    ]

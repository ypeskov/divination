# Generated by Django 4.0.3 on 2022-03-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runes', '0011_remove_question_ip_address_question_origin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.JSONField(default=0),
            preserve_default=False,
        ),
    ]
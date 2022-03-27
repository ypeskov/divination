# Generated by Django 4.0.3 on 2022-03-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runes', '0008_alter_rune_img_direct_alter_rune_img_inverted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
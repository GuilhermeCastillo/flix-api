# Generated by Django 5.0.2 on 2024-02-29 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genres',
            new_name='genre',
        ),
    ]
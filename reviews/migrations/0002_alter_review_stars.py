# Generated by Django 5.0.2 on 2024-02-29 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Avaliacao nao pode ser inferior a 0 estrelas.'), django.core.validators.MaxValueValidator(5, 'Avaliacao nao pode ser superior a 5 estrelas.')]),
        ),
    ]
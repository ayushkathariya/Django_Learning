# Generated by Django 5.0.1 on 2024-03-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]

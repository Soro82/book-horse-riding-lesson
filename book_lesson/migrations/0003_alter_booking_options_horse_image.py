# Generated by Django 4.2.13 on 2024-05-28 18:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_lesson', '0002_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-lesson_date']},
        ),
        migrations.AddField(
            model_name='horse',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
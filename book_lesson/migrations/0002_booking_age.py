# Generated by Django 4.2.13 on 2024-07-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='age',
            field=models.IntegerField(blank=True, choices=[(0, 'Child'), (1, 'Adult')], default=0),
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitem',
            name='discover_link',
            field=models.URLField(default='/'),
        ),
    ]
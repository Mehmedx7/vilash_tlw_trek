# Generated by Django 5.0.1 on 2024-03-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='brochure_pdf',
        ),
        migrations.AddField(
            model_name='package',
            name='Itinerary_link',
            field=models.URLField(default='/'),
        ),
    ]

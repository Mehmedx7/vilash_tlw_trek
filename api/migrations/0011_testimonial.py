# Generated by Django 5.0.1 on 2024-03-25 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_the_world_popular_destination_itinerary_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='Testimonial')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('star', models.CharField(max_length=200)),
            ],
        ),
    ]

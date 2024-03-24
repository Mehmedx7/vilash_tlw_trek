# Generated by Django 5.0.1 on 2024-03-24 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_popular_destination_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_Destination_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.popular_destination_category')),
            ],
        ),
        migrations.CreateModel(
            name='Popular_Destination_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='destination_images/')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.popular_destination_place')),
            ],
        ),
    ]

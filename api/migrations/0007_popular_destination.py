# Generated by Django 5.0.1 on 2024-03-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_popular_destination_place_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Popular_Destination')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
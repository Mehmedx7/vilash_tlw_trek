# Generated by Django 5.0.1 on 2024-03-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel_images')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
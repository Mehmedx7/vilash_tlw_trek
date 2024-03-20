# Generated by Django 5.0.1 on 2024-03-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_carouselitem_discover_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='package_images')),
                ('location', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('pax', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('star', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('brochure_pdf', models.FileField(blank=True, null=True, upload_to='package_pdf')),
            ],
        ),
    ]

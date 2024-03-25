from django.db import models

# Create your models here.
class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel_images')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    discover_link = models.URLField(default='/')

    def __str__(self):
        return self.title
    
class Package(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='package_images')
    location = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    pax = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    star = models.CharField(max_length=200)
    description = models.TextField()
    Itinerary_link = models.URLField(default='/')

    def __str__(self):
        return self.title

class Popular_Destination(models.Model):
    image = models.ImageField(upload_to='Popular_Destination')
    name = models.CharField(max_length=100)
    Itinerary_link = models.URLField(default='/')

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class The_World(models.Model):
    image = models.ImageField(upload_to='The_World')
    name = models.CharField(max_length=100)
    Discount_Percentage = models.PositiveIntegerField()
    Itinerary_link = models.URLField(default='/')

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='Testimonial')
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    star = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class seo(models.Model):
    keywords = models.TextField()
    description = models.TextField()

    def __str__(self):
        return ' '.join(self.keywords.split()[:10])
    
    

    
    




    


from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):   
    carousel_items = CarouselItem.objects.all()
    packages = Package.objects.all()
    Popular_Dest = Popular_Destination.objects.all()
    gallery = Gallery.objects.all()
    explore = The_World.objects.all()
    Testimonials = Testimonial.objects.all()
    Seo = seo.objects.all()
    context = {
        'carousel_items': carousel_items,
        'packages': packages,
        'Popular_Dest': Popular_Dest,
        'gallery': gallery,
        'explore': explore,
        'Testimonials': Testimonials,
        'Seo': Seo
    }
    return render(request, 'index.html', context)



def About(request):    
    return render(request, 'about.html')

def Services(request):    
    return render(request, 'services.html')

def Packages(request):    
    carousel_items = CarouselItem.objects.all()
    packages = Package.objects.all()
    Popular_Dest = Popular_Destination.objects.all()
    gallery = Gallery.objects.all()
    explore = The_World.objects.all()
    Testimonials = Testimonial.objects.all()
    context = {
        'carousel_items': carousel_items,
        'packages': packages,
        'Popular_Dest': Popular_Dest,
        'gallery': gallery,
        'explore': explore,
        'Testimonials': Testimonials
    }
    return render(request, 'packages.html', context)

def Blogs(request):    
    return render(request, 'blogs.html')

def Contact(request):    
    return render(request, 'contact.html')

def Register(request):    
    return render(request, 'register.html')
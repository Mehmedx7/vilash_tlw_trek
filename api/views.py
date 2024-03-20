from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):   
    carousel_items = CarouselItem.objects.all()
    packages = Package.objects.all()
    context = {
        'carousel_items': carousel_items,
        'packages': packages
    }
    return render(request, 'index.html', context)

def About(request):    
    return render(request, 'about.html')

def Services(request):    
    return render(request, 'services.html')

def Packages(request):    
    return render(request, 'packages.html')

def Blogs(request):    
    return render(request, 'blogs.html')

def Contact(request):    
    return render(request, 'contact.html')

def Register(request):    
    return render(request, 'register.html')
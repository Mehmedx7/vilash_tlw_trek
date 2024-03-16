from django.shortcuts import render

# Create your views here.

def Home(request):    
    return render(request, 'index.html')

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
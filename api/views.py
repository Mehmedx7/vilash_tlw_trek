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
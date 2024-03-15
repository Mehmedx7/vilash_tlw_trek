from django.shortcuts import render

# Create your views here.

def Home(request):    
    print("Hello")
    return render(request, 'index.html')
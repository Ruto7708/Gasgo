from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'Index.html')

def Order(request):
    return render(request, 'Order.html')

def About(request):
    return render(request, 'About.html')

def Contactus(request):
    return render(request, 'Contactus.html')

def Services(request):
    return render(request, 'Services.html')
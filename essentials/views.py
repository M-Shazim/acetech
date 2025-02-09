from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'essentials/home.html', {'products': products})

def about(request):
    return render(request, 'essentials/about.html')

def contact(request):
    return render(request, 'essentials/contact.html')

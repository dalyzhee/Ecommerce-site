from django.shortcuts import render
from .models import Product, Category, Service

def index(request):
    products = Product.objects.all()
    services = Service.objects.all()
    context = {
        'products': products,
        'services': services
    }
    return render(request, 'index.html', context)

def product(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {
        'products': products,
        'categorys': categorys
    }
    return render(request, 'product.html', context)

def service(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'service.html', context)

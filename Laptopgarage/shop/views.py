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

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    categorys = Category.objects.all()
    context = {
        'product': product,
        'categorys': categorys
    }
    return render(request, 'product_detail.html', context)

def service(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'service.html', context)

def category(request, category):
    products = Product.objects.filter(categories__name__contains = category)
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'category.html', context)
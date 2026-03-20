from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'home.html')

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse("New Products")

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})


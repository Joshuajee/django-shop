from django.shortcuts import render
from .models import Products

# Create your views here.

def index(req):
    products = Products.objects.all()
    return render(req, "index.html", {'products': products})

def product_page(req, slug):
    product = Products.objects.get(slug= slug)
    return render(req, 'products.html', {"product": product})

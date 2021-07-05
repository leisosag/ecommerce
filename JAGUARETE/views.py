from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .forms import ProductForm
from .models import Product, Cart

# products = ['producto 1', 'producto 2', 'producto 3', 'producto 4', 'producto 5']

# Create your views here.
def index(request):
    all_products_reversed = Product.objects.all()[::-1]
    products = all_products_reversed[:11]
    latest_products = products[:3]
    all_latest_products = products[3:-1]
    return render(request, "JAGUARETE/index.html", {
        # "products": request.session["products"]
        'products': all_latest_products,
        'latest_products': latest_products
    })

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "JAGUARETE/product.html", {
        'product': product
    })

def product_add(request):
    submitted = False
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product_add?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "JAGUARETE/product_add.html", {
        'form': form,
        'submitted': submitted
    })

def product_edit(request, product_id):
    submitted = False
    product = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
            form.save()
            return render(request, "JAGUARETE/index.html", {
                'products': Product.objects.all()
            })
    return render(request, "JAGUARETE/product_edit.html", {
        'product': product,
        'form': form
    })

def about(request):
    return render(request, "JAGUARETE/about.html")

def contact(request):
    return render(request, "JAGUARETE/contact.html")

def login(request):
    return render(request, "JAGUARETE/login.html")

def register(request):
    return render(request, "JAGUARETE/register.html")

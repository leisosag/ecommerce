from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import ProductForm
from .models import Product, Cart, Categories

# Create your views here.
def index(request):
    all_products_reversed = Product.objects.all()[::-1]
    products = all_products_reversed[:11]
    latest_products = products[:3]
    all_latest_products = products[3:-1]
    return render(request, "JAGUARETE/index.html", {
        'products': all_latest_products,
        'latest_products': latest_products
    })

def categories(request):
    return render(request, "JAGUARETE/categories.html", {
        'categories': Categories.objects.all()
    })

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "JAGUARETE/product.html", {
        'product': product
    })

def cart(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "JAGUARETE/cart.html", {
        'product': product
    })

def product_add(request):
    submitted = False
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
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

def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return render(request, "JAGUARETE/index.html", {
        'products': Product.objects.all()
    })

def search_results(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        products = Product.objects.filter(title__contains=search_term)
        return render(request, "JAGUARETE/search_results.html", {
            'search_term': search_term,
            'products': products,
        })
    else:
        return render(request, "JAGUARETE/search_results.html")

def search_category(request):
    return render(request, "JAGUARETE/search_category.html")

def about(request):
    return render(request, "JAGUARETE/about.html")

def contact(request):
    return render(request, "JAGUARETE/contact.html")


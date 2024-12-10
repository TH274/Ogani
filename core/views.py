from django.shortcuts import render
from django.http import HttpResponse
from core.models import Product, CartOrder, Category, Vendor, CartOrderItems, ProductImages, ProductReview, wishlist, Address



def index(request):
    product = Product.objects.all()

    context = {
        "products": product
    }

    return render(request, 'core/index.html', context)

def shop_grid(request):
    return render(request, 'core/shop-grid.html')

def shop_details(request):
    return render(request, 'core/shop-details.html')

def shoping_cart(request):
    return render(request, 'core/shoping-cart.html')

def contact(request):
    return render(request, 'core/contact.html')

def checkout(request):
    return render(request, 'core/checkout.html')

def blog(request):
    return render(request, 'core/blog.html')

def blog_details(request):
    return render(request, 'core/blog-details.html')
from django.shortcuts import render
from .models import Product
from .utils import get_user_city, filter_products



def main_page(request):
    template = "index.html"
    return render(request, template)

def faq_page(request):
    template = "faq.html"
    return render(request, template)

def loans_page(request):
    template = "loans.html"

    city = get_user_city(request)
    if request.method == 'GET':
        products = filter_products(request)
    else:
        products = Product.objects.all()
    return render(request, template, {'city': city, 'products': products})

def invest_page(request):
    template = "invest.html"
    
    city = get_user_city(request)
    return render(request, template, {'city': city})



from django.shortcuts import render
from .models import Product


def main_page(request):
    return None

def faq_page(request):
    template = "faq.html"
    return render(request, template)


    


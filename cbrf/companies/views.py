from django.shortcuts import render
from .models import Company


def main_page(request):
    template = "test.html"
    return render(request, template)



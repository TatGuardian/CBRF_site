from django.shortcuts import render


def main_page(request):
    template = "index.html"
    return render(request, template)

def organizations_page(request):
    template = "organizations.html"
    return render(request, template)

def faq_page(request):
    template = "faq.html"
    return render(request, template)
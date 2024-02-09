from django.shortcuts import render


def main_page(request):
    template = "test.html"
    return render(request, template)



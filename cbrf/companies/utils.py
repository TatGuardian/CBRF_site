from ipware import get_client_ip
import requests

from django.db.models import Q
from .models import Product


def get_user_city(request):
    ip, _ = get_client_ip(request)
    if ip:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            data = response.json()
            country = data.get('country')
            city = data.get('city')
            if country == 'Russia':
                return city
    return 'Москва'

def filter_products(request):

    method = request.GET.get('method')
    print(method)
    term = request.GET.get('term')

    # Фильтруем продукты в соответствии с переданными параметрами
    products = Product.objects.all()
    if method:
        products = products.filter(method_reg=method)
    if term:
        # Фильтруем продукты, чтобы срок займа был между term_min и term_max
        products = products.filter(Q(term_min__lte=term) & Q(term_max__gte=term))
    
    return products
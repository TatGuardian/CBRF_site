from django.shortcuts import render
from .models import News
from companies.models import Product
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


def main_page(request):
    img_news = News.objects.exclude(image=None).order_by('-date')[:1]
    non_img_news = News.objects.exclude(id__in=[news.id for news in img_news] or news.image!=None).order_by('-date')[:2]
    news = list(img_news) + list(non_img_news)

    cbr_data = get_cbr_data(url = 'https://cbr.ru')
    translated_data = {
        'inflation': cbr_data.get('Инфляция'),
        'key_rate': cbr_data.get('Ключевая ставка'),
        'RUONIA_rate': cbr_data.get('Ставка RUONIA')
    }

    exchange_rates_data = get_cbr_rates_data(url = 'https://cbr.ru')

    products = Product.objects.order_by('?')[:4]

    return render(request, 'index.html', {'news': news, 'cbr_data': translated_data, 'exchange_rates_data': exchange_rates_data, 'products': products})

def get_cbr_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    indicators = soup.find_all('div', class_='main-indicator')

    data = {}

    for indicator in indicators:
        indicator_sub = indicator.find('div', class_='main-indicator_sub')
        indicator_value = indicator.find('div', class_='main-indicator_value')
        if indicator_sub and indicator_value:
            indicator_name = indicator_sub.text.strip()
            indicator_value = indicator_value.text.strip()
            data[indicator_name] = indicator_value

    return data

def get_cbr_rates_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    indicators = soup.find_all('div', class_='main-indicator_rates-table')
    soup = BeautifulSoup(response.text, 'lxml')
    rate_elements = soup.find_all(class_='main-indicator_rate')
    
    data = {}

    for rate_element in rate_elements:

        currency_name = rate_element.find(class_='col-md-2').get_text(strip=True)[:3]
        rate_values = rate_element.find_all(class_='mono-num')
        if len(rate_values) >= 2:
            y_rate = rate_values[0].get_text(strip=True)
            t_rate = rate_values[1].get_text(strip=True)
            data[currency_name] = (y_rate, t_rate)

    return data
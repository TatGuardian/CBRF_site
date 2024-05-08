from django.contrib import admin
from django.urls import path
from .views import faq_page, invest_page, loans_page, main_page

app_name = 'companies'

urlpatterns = [
    path('faq.html', faq_page, name='faq'),
    path('loans.html', loans_page, name='loans'),
    path('loans/', loans_page, name='loans'),
    path('invest.html', invest_page, name='invest'),
    path('invest/', invest_page, name='invest'),
    path('', main_page, name='main'),
]

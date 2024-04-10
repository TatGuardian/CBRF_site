from django.contrib import admin
from django.urls import path
from .views import main_page, organizations_page, faq_page

app_name = 'companies'

urlpatterns = [
    path('faq.html', faq_page, name='faq'),
    path('organizations.html', organizations_page, name='organizations'),
    path('index.html', main_page, name='main'),
    path('', main_page, name='main'),
]

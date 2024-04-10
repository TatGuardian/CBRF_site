from django.contrib import admin
from django.urls import path
from .views import main_page

app_name = 'news'

urlpatterns = [
    path('', main_page),
]

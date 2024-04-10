from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.NewsCategories)
admin.site.register(models.Tags)
admin.site.register(models.News)
admin.site.register(models.News_Tags)
